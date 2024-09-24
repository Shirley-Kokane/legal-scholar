import streamlit as st

from chat import clear_chat, display_chat
from database import SupabaseDatabase
from example_chats import get_example_chat, get_example_chat_ids, get_example_chat_title
from login import display_login
from signup import display_signup
from utils import chatType, init_env, logout, mainPageOptions, sessionKeys


def set_display_callback(value: mainPageOptions):
    st.session_state[sessionKeys.DISPLAY] = value


def past_chat_selectbox_callback():
    temp_chat_id: str = st.session_state[sessionKeys.PAST_CHAT_SELECT_BOX]

    if temp_chat_id is None:
        clear_chat()
    else:
        db: SupabaseDatabase = st.session_state[sessionKeys.DATABASE]
        st.session_state[sessionKeys.CHAT_ID] = temp_chat_id

        if temp_chat_id.startswith(f"{chatType.USER.value}-"):
            temp_chat_id = int(temp_chat_id.removeprefix(f"{chatType.USER.value}-"))
            (
                st.session_state[sessionKeys.MESSAGES],
                st.session_state[sessionKeys.GEMINI_HISTORY],
            ) = db.get_chat(st.session_state[sessionKeys.EMAIL], chat_id=temp_chat_id)
        elif temp_chat_id.startswith(f"{chatType.EXAMPLE.value}-"):
            temp_chat_id = int(temp_chat_id.removeprefix(f"{chatType.EXAMPLE.value}-"))
            (
                st.session_state[sessionKeys.MESSAGES],
                st.session_state[sessionKeys.GEMINI_HISTORY],
            ) = get_example_chat(temp_chat_id)

        st.session_state[sessionKeys.CHAT] = st.session_state[
            sessionKeys.MODEL
        ].start_chat(history=st.session_state[sessionKeys.GEMINI_HISTORY])


def side_bar():
    # print("side_bar")
    # Sidebar allows a list of past chats
    with st.sidebar:
        if not st.session_state[sessionKeys.LOGGED_IN]:
            st.write("Sign up or Login to save and retrive chats!")

            st.button(
                label="Sign Up",
                on_click=set_display_callback,
                args=[mainPageOptions.SIGNUP],
            )
            st.button(
                label="Log In",
                on_click=set_display_callback,
                args=[mainPageOptions.LOGIN],
            )
            if st.session_state[sessionKeys.DISPLAY] != mainPageOptions.CHAT:
                st.button(
                    label="Back to chat",
                    on_click=set_display_callback,
                    args=[mainPageOptions.CHAT],
                )

            if st.session_state[sessionKeys.DISPLAY] == mainPageOptions.CHAT:
                st.button(label="Clear chat", on_click=clear_chat)
            # st.write("# Example Chats")
            # label = "Pick an example chat"
        else:
            st.write(
                f"# Welcome {st.session_state[sessionKeys.USERNAME].split(' ')[0]}"
            )
            st.button(label="Logout", on_click=logout)

            st.button(label="New chat", on_click=clear_chat)

            # st.write("# Past Chats")
            # label = "Pick a past chat"

        past_chat_ids: dict = st.session_state[sessionKeys.PAST_CHAT_IDS]

        all_keys = [
            f"{chatType.USER.value}-{chat_id}"
            for chat_id in sorted(
                list(past_chat_ids.keys()),
                reverse=True,
            )
        ]

        # all_keys += [
        #     f"{chatType.EXAMPLE.value}-{chat_id}" for chat_id in get_example_chat_ids()
        # ]

        def format_function(chat_id: str):

            if chat_id.startswith(f"{chatType.USER.value}-"):
                chat_id = int(chat_id.removeprefix(f"{chatType.USER.value}-"))
                return f"({chat_id}) {past_chat_ids.get(chat_id)}"

            chat_id = int(chat_id.removeprefix(f"{chatType.EXAMPLE.value}-"))
            return f"(Example {chat_id}) {get_example_chat_title(chat_id)}"

        # st.selectbox(
        #     label=label,
        #     options=all_keys,
        #     index=None,
        #     format_func=format_function,
        #     key=sessionKeys.PAST_CHAT_SELECT_BOX,
        #     on_change=past_chat_selectbox_callback,
        # )

        if not st.session_state[sessionKeys.LOGGED_IN]:
            st.markdown(
                "Please Sign Up to for upcoming features:\n- Lawyer recommendation for your case in other state.\n- More Details about the Lawyers per case."
            )


def main_display():
    # print("main_display")
    if st.session_state[sessionKeys.DISPLAY] == mainPageOptions.SIGNUP:
        display_signup()
    elif st.session_state[sessionKeys.DISPLAY] == mainPageOptions.LOGIN:
        display_login()
    else:
        display_chat()


def main():
    if sessionKeys.LOGGED_IN not in st.session_state:
        init_env()

    side_bar()
    main_display()


# print("----------------- Done -------------------")


if __name__ == "__main__":
    main()
