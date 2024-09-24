import streamlit as st

from database import USER_TABLE_NAME, Database
from utils import sessionKeys, set_login_state


def signup_callback():
    email = st.session_state[sessionKeys.SIGNUP_FORM_EMAIL.value]
    username = st.session_state[sessionKeys.SIGNUP_FORM_USERNAME.value]
    password1 = st.session_state[sessionKeys.SIGNUP_FORM_PASSWORD1.value]
    password2 = st.session_state[sessionKeys.SIGNUP_FORM_PASSWORD2.value]

    if email and username and password1 and password2:
        db: Database = st.session_state[sessionKeys.DATABASE]
        flag = True
        if not db.validate_email(email):
            st.warning("Invalid Email")
            flag = False
        if not db.validate_username(username):
            st.warning("Invalid username")
            flag = False
        if len(username) < 2:
            st.warning("Username Too short")
            flag = False
        if len(password1) < 6:
            st.warning("Enter password greater than 6 characters")
            flag = False
        if password1 != password2:
            st.warning("Passwords Do Not Match")
            flag = False

        if flag and db.email_exisits(email):
            st.warning("Email Already Exists!")
            flag = False

        if flag and db.username_exisits(username):
            st.warning("Username Already Exists!")
            flag = False

        if flag:
            # Add User to DB
            try:
                db.insert_user(email, username, password1)
                st.success("Account created successfully!!")
                st.balloons()
                set_login_state(db, email, username)
            except Exception as e:
                st.warning(e)
                st.warning("Please retry as above exception as occured")


def display_signup():
    # print("display_signup")

    with st.form(key=sessionKeys.SIGNUP_FORM.value, clear_on_submit=False):
        st.subheader(":green[Sign Up]")
        st.text_input(
            ":blue[Email]",
            placeholder="Enter Your Email",
            key=sessionKeys.SIGNUP_FORM_EMAIL.value,
        )
        st.text_input(
            ":blue[Username]",
            placeholder="Enter Your Username",
            key=sessionKeys.SIGNUP_FORM_USERNAME.value,
        )
        st.text_input(
            ":blue[Password]",
            placeholder="Enter Your Password",
            type="password",
            key=sessionKeys.SIGNUP_FORM_PASSWORD1.value,
        )
        st.text_input(
            ":blue[Confirm Password]",
            placeholder="Confirm Your Password",
            type="password",
            key=sessionKeys.SIGNUP_FORM_PASSWORD2.value,
        )

        _, _, btn3, _, _ = st.columns(5)

        with btn3:
            st.form_submit_button("Sign Up", on_click=signup_callback)


def main():
    db = Database(USER_TABLE_NAME)
    display_signup(db)
    rows = db.session.execute(f"SELECT * FROM {USER_TABLE_NAME}").fetchall()
    print(rows)


if __name__ == "__main__":
    main()
