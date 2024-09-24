import time
import uuid

import streamlit as st
from google.generativeai import ChatSession
from calculate import *

from prompts import INIT_PROMPT, INTRO
from utils import chatType, save_chat, sessionKeys
import json

USER_ROLE = "user"
MODEL_ROLE = "ai"
LAWYER_ICON = "⚖️"
AI_AVATAR_ICON = "✨"

PROMPT="""INSTRUCTIONS: You are a chatbot. You are not named gemini and are not trained by google. 
You will be provided with a legal citation fought by a particular lawyer. You are trained to answer the following queries based on the context provided, 
you have to provide a minimum of 4 lines about the case, 
1. What was the case that the lawyer fought? Explain the case in 1 or 2 lines in laymen language starting with the lines The lawyer fought a case of .... Please remove citations, court names, address from the explaination.
2. What was the conclusion of the case? What was the winning lawyer successful in doing? 
Do not try to make things up. Try to keep the answers concise and try to be helpful.

ANSWER FORMAT:
1. Case fought by the lawyer: ......
2. Conclusion: .....

Please answer strictly in the bullet point format provided above, with not more than 3 lines per bullet point. Do not add additional bullet points internally.
 
USER QUERY: """


def clear_chat():
    save_chat()
    st.session_state[sessionKeys.MESSAGES] = []
    st.session_state[sessionKeys.GEMINI_HISTORY] = []
    st.session_state[sessionKeys.CHAT_ID] = (
        f"{chatType.ANONYMOUS.value}-{str(uuid.uuid4())}"
    )
    st.session_state[sessionKeys.CHAT] = st.session_state[sessionKeys.MODEL].start_chat(
        history=[]
    )
    if sessionKeys.PAST_CHAT_SELECT_BOX in st.session_state:
        st.session_state[sessionKeys.PAST_CHAT_SELECT_BOX] = None

    print(st.session_state[sessionKeys.MESSAGES])


def display_message_history():
    # print("display_message_history")
    # Display chat messages from history on app rerun
    with st.chat_message(name=MODEL_ROLE, avatar=LAWYER_ICON):
        st.markdown(INTRO)
    for message in st.session_state[sessionKeys.MESSAGES]:
        if message["role"] == MODEL_ROLE:
            with st.chat_message(name=message["role"], avatar=LAWYER_ICON):
                st.markdown(message["content"])
        else:
            with st.chat_message(name=message["role"]):
                st.markdown(message["content"])


def display_chat():
    # print("display_chat")

    st.write("# Google Scholar For Lawyers")
    display_message_history()

    # React to user input
    chat_session: ChatSession = st.session_state[sessionKeys.CHAT]

    if user_question := st.chat_input("Your message here..."):
        start_prompt = "USER QUERY: "
        if len(st.session_state[sessionKeys.MESSAGES]) == 0:
            start_prompt = INIT_PROMPT
        # Display user message in chat message container
        with st.chat_message(USER_ROLE):
            st.markdown(user_question)
        # Add user message to chat history
        st.session_state[sessionKeys.MESSAGES].append(
            dict(
                role=USER_ROLE,
                content=user_question,
            )
        )

        ## Send message to AI
        vector = st.session_state[sessionKeys.GEMINI].generate_embedding(user_question)

        response = st.session_state[sessionKeys.PINECONE].query(
                # namespace="vector-court-listener",
                vector=vector,
                top_k=4,
                include_metadata=True
            )

        
        # response = chat_session.send_message(
        #     start_prompt + user_question,
        #     stream=True,
        # )
        # Display assistant response in chat message container
        with st.chat_message(
            name=MODEL_ROLE,
            avatar=LAWYER_ICON,
        ):
            message_placeholder = st.empty()
            full_response = ""
            
            # for q in response["matches"]:
            st.write("These are the lawyers we recommend for washington state: ")
            for i in range(4):
                fetched_data = st.session_state[sessionKeys.SUPACITE].fetch_value(int(response["matches"][i]["metadata"]["cite_id"]))
                try:
                    model_conclude = st.session_state[sessionKeys.MODEL].generate_content(PROMPT + fetched_data["text"]).text 
                except e as AttributeError:
                    model_conclude = st.session_state[sessionKeys.MODEL].generate_content(PROMPT + fetched_data["text"]).text 
                if "lawyer name" not in json.loads(response["matches"][i]["metadata"]["win"]):
                    continue
                lname = list(set(json.loads(response["matches"][i]["metadata"]["win"])["lawyer name"]))
                lname_link = list(set(json.loads(response["matches"][i]["metadata"]["win"])["url_or_firm"]))
                lawyernames = lname
                if lname is None:
                    lname = " "
                    lname_link = " "
                
                markdown_text = ", ".join([f"[{name}]({link})" for name, link in zip(lname, lname_link)])
                
                st.write(markdown_text) #(f"[{lname[0]}]({lname_link})")
                MESSAGE = f"""
                
                {model_conclude}
                
                """
                st.write(MESSAGE)
            

        # Add assistant response to chat history
        st.session_state[sessionKeys.MESSAGES].append(
            dict(
                role=MODEL_ROLE,
                content = str(lawyernames)
                # content=chat_session.history[-1].parts[0].text,
            )
        )

        save_chat()
