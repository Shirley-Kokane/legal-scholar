import streamlit as st

from database import USER_TABLE_NAME, Database
from utils import sessionKeys, set_login_state


def login_callback():

    email = st.session_state[sessionKeys.LOGIN_FORM_EMAIL.value]
    password = st.session_state[sessionKeys.LOGIN_FORM_PASSWORD.value]

    if email and password:
        db: Database = st.session_state[sessionKeys.DATABASE]
        flag = True
        if not db.validate_email(email):
            st.warning("Invalid Email")
            flag = False
        if len(password) < 6:
            st.warning("Enter password greater than 6 characters")
            flag = False

        if flag and not db.email_exisits(email):
            st.warning("Email Does not exist! Please sign up first")
            flag = False

        if flag:
            check, username = db.check_email_password(email, password)
            if check:
                st.success("Account logged in successfully!!")
                st.balloons()
                set_login_state(db, email, username)
            else:
                st.warning("Credentials do not match!")


def display_login():
    # print("display_login")

    with st.form(key=sessionKeys.LOGIN_FORM.value, clear_on_submit=False):
        st.subheader(":green[Log In]")
        st.text_input(
            ":blue[Email]",
            placeholder="Enter Your Email",
            key=sessionKeys.LOGIN_FORM_EMAIL.value,
        )
        st.text_input(
            ":blue[Password]",
            placeholder="Enter Your Password",
            type="password",
            key=sessionKeys.LOGIN_FORM_PASSWORD.value,
        )

        _, _, btn3, _, _ = st.columns(5)

        with btn3:
            st.form_submit_button(
                "Login",
                on_click=login_callback,
            )


def main():
    db = Database(USER_TABLE_NAME)
    display_login(db)
    rows = db.session.execute(f"SELECT * FROM {USER_TABLE_NAME}").fetchall()
    print(rows)


if __name__ == "__main__":
    main()
