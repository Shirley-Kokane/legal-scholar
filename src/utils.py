import uuid
from enum import Enum
from pinecone import Pinecone, ServerlessSpec

import google.generativeai as genai
import streamlit as st
from google.generativeai import ChatSession
from calculate import *
from client import OpenAIClient

from database import (
    Database,
    ANONYMOUS_CHAT_TABLE_NAME,
    CHAT_TABLE_NAME,
    USER_TABLE_NAME,
    SupabaseDatabase,SupabaseHandler
)

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]


class sessionKeys(Enum):
    MODEL = "model"
    GEMINI = "gemini"
    PINECONE = "pincone"
    LOGGED_IN = "loggedin"
    CHAT_ID = "chat_id"
    MESSAGES = "messages"
    GEMINI_HISTORY = "gemini_history"
    CHAT = "chat"
    PAST_CHAT_IDS = "past_chat_ids"
    DISPLAY = "display"
    EMAILDATABASE = "emaildatabase"
    DATABASE = "database"
    SUPACITE = "datacite"
    USERNAME = "username"
    EMAIL = "email"
    PAST_CHAT_SELECT_BOX = "past_chat_select_box"

    SIGNUP_FORM = "signup_form"
    LOGIN_FORM = "login_form"

    SIGNUP_FORM_EMAIL = "signup_form_email"
    SIGNUP_FORM_USERNAME = "signup_form_username"
    SIGNUP_FORM_PASSWORD1 = "signup_form_password1"
    SIGNUP_FORM_PASSWORD2 = "signup_form_password2"

    LOGIN_FORM_EMAIL = "login_form_email"
    LOGIN_FORM_PASSWORD = "login_form_password"


class mainPageOptions(Enum):
    LOGIN = "login"
    SIGNUP = "signup"
    CHAT = "chat"


class chatType(Enum):
    USER = "user"
    ANONYMOUS = "anonumous"
    EXAMPLE = "example"


def set_login_state(db: SupabaseDatabase, email: str, username: str):
    # print("set_login_state")
    st.session_state[sessionKeys.LOGGED_IN] = True
    st.session_state[sessionKeys.DISPLAY] = mainPageOptions.CHAT
    st.session_state[sessionKeys.USERNAME] = username
    st.session_state[sessionKeys.EMAIL] = email
    past_chat_ids = db.get_all_chat_ids(email)
    st.session_state[sessionKeys.PAST_CHAT_IDS] = {
        data[0]: data[1] for data in past_chat_ids
    }

    save_chat(from_login_signup=True)


def reset_state_variables():
    # print("reset_state_variables")

    if sessionKeys.LOGGED_IN in st.session_state:
        save_chat()

    st.session_state[sessionKeys.LOGGED_IN] = False
    st.session_state[sessionKeys.USERNAME] = None
    st.session_state[sessionKeys.EMAIL] = None
    st.session_state[sessionKeys.PAST_CHAT_IDS] = {}
    st.session_state[sessionKeys.CHAT_ID] = (
        f"{chatType.ANONYMOUS.value}-{str(uuid.uuid4())}"
    )
    st.session_state[sessionKeys.MESSAGES] = []
    st.session_state[sessionKeys.GEMINI_HISTORY] = []
    st.session_state[sessionKeys.CHAT] = st.session_state[sessionKeys.MODEL].start_chat(
        history=[]
    )
    st.session_state[sessionKeys.DISPLAY] = mainPageOptions.CHAT


def logout():
    # print("Logout")
    reset_state_variables()


def init_env():
    # print("init_env")

    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    cn = Config("/export/home/ps/repo/lawvector/config.yaml")
    st.session_state[sessionKeys.MODEL] = genai.GenerativeModel(
         "gemini-pro", safety_settings
     )
    st.session_state[sessionKeys.GEMINI] = OpenAIClient() #GeminiEmbed(cn)

    pc = Pinecone(api_key=st.secrets["PINECONE_API_KEY"])
    st.session_state[sessionKeys.PINECONE] = pc.Index("vector-listener-court")
    
    st.session_state[sessionKeys.SUPACITE] = SupabaseHandler(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"] , st.secrets["TABLE_NAME"])
    reset_state_variables()
    st.session_state[sessionKeys.EMAILDATABASE] = Database(USER_TABLE_NAME, CHAT_TABLE_NAME)
    st.session_state[sessionKeys.DATABASE] = SupabaseDatabase(
        USER_TABLE_NAME, CHAT_TABLE_NAME, ANONYMOUS_CHAT_TABLE_NAME
    )


def save_chat(from_login_signup=False):
    if len(st.session_state[sessionKeys.MESSAGES]) == 0:
        return
    chat_id: str = st.session_state[sessionKeys.CHAT_ID]
    if chat_id.startswith(f"{chatType.EXAMPLE.value}-") and not from_login_signup:
        return

    db: SupabaseDatabase = st.session_state[sessionKeys.DATABASE]
    chat_session: ChatSession = st.session_state[sessionKeys.CHAT]

    if st.session_state[sessionKeys.LOGGED_IN]:

        if not chat_id.startswith(f"{chatType.USER.value}-"):
            next_chat_id = db.get_next_chat_id(st.session_state[sessionKeys.EMAIL])
            chat_id = f"{chatType.USER.value}-{next_chat_id}"
            st.session_state[sessionKeys.CHAT_ID] = chat_id

        chat_name = st.session_state[sessionKeys.MESSAGES][0]["content"]
        chat_id = int(chat_id.removeprefix(f"{chatType.USER.value}-"))
        db.save_chat(
            st.session_state[sessionKeys.EMAIL],
            chat_id,
            chat_name,
            st.session_state[sessionKeys.MESSAGES],
            chat_session.history,
        )

        st.session_state[sessionKeys.PAST_CHAT_IDS][chat_id] = chat_name
    else:
        chat_id = chat_id.removeprefix(f"{chatType.ANONYMOUS.value}-")
        db.save_anonymous_chat(
            chat_id,
            st.session_state[sessionKeys.MESSAGES],
        )
