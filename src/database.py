import datetime
import json
import re

import streamlit as st
from google.ai import generativelanguage as glm
from sqlalchemy import text
from streamlit_authenticator.utilities.hasher import Hasher
from supabase import Client, create_client

USER_TABLE_NAME = "users"
CHAT_TABLE_NAME = "chats"
ANONYMOUS_CHAT_TABLE_NAME = "anonymous_chat"


def convert_gemini_history_to_json(history: list[glm.Content]):
    json_history = []
    for value in history:
        json_history.append(dict(text=value.parts[0].text, role=value.role))

    return json_history


def convert_json_to_gemini_history(json_history: list[dict]):
    gemini_history = []
    for value in json_history:
        part = glm.Part(text=value["text"])
        gemini_history.append(glm.Content(parts=[part], role=value["role"]))

    return gemini_history


class Database:
    def __init__(self, user_table_name, chat_table_name) -> None:
        # self.database_name = database_name
        self.user_table_name = user_table_name
        self.chat_table_name = chat_table_name

        self.connection = st.connection("credentials", type="sql")
        # self.connection = st.connection("supabase", type=SupabaseConnection)

        with self.connection.session as session:
            session.execute(
                text(
                    f"CREATE TABLE IF NOT EXISTS {self.user_table_name} (email TEXT NOT NULL PRIMARY KEY, username TEXT NOT NULL UNIQUE, hashed_password TEXT NOT NULL, date_joined TIMESTAMP NOT NULL);"
                )
            )

            session.execute(
                text(
                    f"CREATE TABLE IF NOT EXISTS {self.chat_table_name} (chat_id INTEGER NOT NULL, email TEXT NOT NULL, chat_name TEXT NOT NULL, message_history TEXT NOT NULL, gemini_history TEXT NOT NULL, PRIMARY KEY (chat_id, email), FOREIGN KEY(email) REFERENCES {self.user_table_name}(email));"
                )
            )
            session.commit()

    def username_exisits(self, username):
        with self.connection.session as session:
            data = session.execute(
                text(
                    f"SELECT count(*) FROM {self.user_table_name} WHERE username = :username;"
                ),
                dict(username=username),
            ).fetchone()[0]

        if data == 0:
            return False
        return True

    def email_exisits(self, email):
        with self.connection.session as session:
            data = session.execute(
                text(
                    f"SELECT count(*) FROM {self.user_table_name} WHERE email = :email"
                ),
                dict(email=email),
            ).fetchone()[0]
        if data == 0:
            return False
        return True

    def insert_user(self, email, username, password):
        """
        Inserts Users into the DB
        :param email:
        :param username:
        :param password:
        :return User Upon successful Creation:
        """
        date_joined = datetime.datetime.now()

        hashed_password = Hasher([password]).generate()[0]

        with self.connection.session as session:
            session.execute(
                text(
                    f"INSERT INTO {self.user_table_name} VALUES (:email, :username, :hashed_password, :date_joined);"
                ),
                dict(
                    email=email,
                    username=username,
                    hashed_password=hashed_password,
                    date_joined=date_joined,
                ),
            )
            session.commit()

    def validate_email(self, email):
        """
        Check Email Validity
        :param email:
        :return True if email is valid else False:
        """
        pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"  # tesQQ12@gmail.com

        if re.match(pattern, email):
            return True
        return False

    def validate_username(self, username):
        """
        Checks Validity of userName
        :param username:
        :return True if username is valid else False:
        """

        pattern = "^[a-zA-Z0-9]*$"
        if re.match(pattern, username):
            return True
        return False

    def check_email_password(self, email, password):
        with self.connection.session as session:
            data = session.execute(
                text(
                    f"SELECT username, hashed_password FROM {self.user_table_name} WHERE email = :email"
                ),
                dict(email=email),
            ).fetchone()

        if data is not None:
            username, hashed_password = data
            return Hasher.check_pw(password, hashed_password), username

        return False, None

    def save_chat(self, email, chat_id, chat_name, message_history, gemini_history):
        gemini_json_history = convert_gemini_history_to_json(gemini_history)

        assert gemini_history == convert_json_to_gemini_history(
            gemini_json_history
        ), "Converted history do not match"

        with self.connection.session as session:
            session.execute(
                text(
                    f"INSERT OR REPLACE INTO {self.chat_table_name} VALUES (:chat_id, :email, :chat_name, :message_history, :gemini_history)"
                ),
                dict(
                    chat_id=chat_id,
                    email=email,
                    chat_name=chat_name,
                    message_history=json.dumps(message_history),
                    gemini_history=json.dumps(gemini_json_history),
                ),
            )
            session.commit()

    def get_all_chat_ids(self, email):

        with self.connection.session as session:
            data = session.execute(
                text(
                    f"SELECT chat_id, chat_name FROM {self.chat_table_name} WHERE email = :email"
                ),
                dict(email=email),
            ).fetchall()

        return data

    def get_next_chat_id(self, email):
        with self.connection.session as session:
            data = session.execute(
                text(
                    f"SELECT COUNT(*) FROM {self.chat_table_name} WHERE email = :email"
                ),
                dict(email=email),
            ).fetchone()[0]

        return data + 1

    def get_chat(self, email, chat_id):
        with self.connection.session as session:
            data = session.execute(
                text(
                    f"SELECT message_history, gemini_history FROM {self.chat_table_name} WHERE email = :email AND chat_id = :chat_id"
                ),
                dict(email=email, chat_id=chat_id),
            ).fetchall()

        # TODO: more check
        if data is None:
            return [], []
        return json.loads(data[0][0]), convert_json_to_gemini_history(
            json.loads(data[0][1])
        )


class SupabaseDatabase:
    def __init__(
        self, user_table_name, chat_table_name, anonymous_chat_table_name
    ) -> None:
        # self.database_name = database_name
        self.user_table_name = user_table_name
        self.chat_table_name = chat_table_name
        self.anonymous_chat_table_name = anonymous_chat_table_name

        url = st.secrets["SUPABASE_URL2"]
        key = st.secrets["SUPABASE_KEY2"]
        self.connection: Client = create_client(url, key)

        ## Commands to init tables in SUPABASE
        # "CREATE TABLE IF NOT EXISTS users (email TEXT NOT NULL PRIMARY KEY, username TEXT NOT NULL UNIQUE, hashed_password TEXT NOT NULL, date_joined TIMESTAMP NOT NULL);

        # "CREATE TABLE IF NOT EXISTS chats (chat_id INTEGER NOT NULL, email TEXT NOT NULL, chat_name TEXT NOT NULL, message_history TEXT NOT NULL, gemini_history TEXT NOT NULL, PRIMARY KEY (chat_id, email), FOREIGN KEY(email) REFERENCES USERS(email));"

        # "CREATE TABLE IF NOT EXISTS anonymous_chat (chat_id TEXT PRIMARY KEY, message_history TEXT NOT NULL);"

    def username_exisits(self, username):
        data, count = (
            self.connection.table(self.user_table_name)
            .select("username")
            .eq("username", username)
            .execute()
        )
        data = data[1]

        if len(data) == 0:
            return False
        return True

    def email_exisits(self, email):
        data, count = (
            self.connection.table(self.user_table_name)
            .select("email")
            .eq("email", email)
            .execute()
        )
        data = data[1]

        if len(data) == 0:
            return False
        return True

    def insert_user(self, email, username, password):
        """
        Inserts Users into the DB
        :param email:
        :param username:
        :param password:
        :return User Upon successful Creation:
        """

        date_joined = str(datetime.datetime.now())
        hashed_password = Hasher([password]).generate()[0]

        data, count = (
            self.connection.table(self.user_table_name)
            .insert(
                {
                    "email": email,
                    "username": username,
                    "hashed_password": hashed_password,
                    "date_joined": date_joined,
                }
            )
            .execute()
        )

    def validate_email(self, email):
        """
        Check Email Validity
        :param email:
        :return True if email is valid else False:
        """
        pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"  # tesQQ12@gmail.com

        if re.match(pattern, email):
            return True
        return False

    def validate_username(self, username):
        """
        Checks Validity of userName
        :param username:
        :return True if username is valid else False:
        """

        pattern = "^[a-zA-Z0-9]*$"
        if re.match(pattern, username):
            return True
        return False

    def check_email_password(self, email, password):

        data, count = (
            self.connection.table(self.user_table_name)
            .select("username, hashed_password")
            .eq("email", email)
            .execute()
        )

        data = data[1]
        if len(data) == 0:
            return False, None

        return (
            Hasher.check_pw(password, data[0]["hashed_password"]),
            data[0]["username"],
        )

    def save_chat(self, email, chat_id, chat_name, message_history, gemini_history):
        gemini_json_history = convert_gemini_history_to_json(gemini_history)

        assert gemini_history == convert_json_to_gemini_history(
            gemini_json_history
        ), "Converted history do not match"

        data, count = (
            self.connection.table(self.chat_table_name)
            .upsert(
                {
                    "chat_id": chat_id,
                    "email": email,
                    "chat_name": chat_name,
                    "message_history": json.dumps(message_history),
                    "gemini_history": json.dumps(gemini_json_history),
                }
            )
            .execute()
        )

    def save_anonymous_chat(self, chat_id: str, message_history):

         data, count = (
            self.connection.table(self.anonymous_chat_table_name)
            .upsert(
                {
                    "chat_id": chat_id,
                    "message_history": (message_history),
                }
            )
            .execute()
        )

    def get_all_chat_ids(self, email):

        data, count = (
            self.connection.table(self.chat_table_name)
            .select("chat_id, chat_name")
            .eq("email", email)
            .execute()
        )
        data = data[1]

        new_data = []
        for line in data:
            new_data.append((line["chat_id"], line["chat_name"]))

        return sorted(new_data)

    def get_next_chat_id(self, email):
        data, count = (
            self.connection.table(self.chat_table_name)
            .select("email")
            .eq("email", email)
            .execute()
        )
        data = data[1]
        return len(data) + 1

    def get_chat(self, email: str, chat_id: int):
        data, count = (
            self.connection.table(self.chat_table_name)
            .select("message_history, gemini_history")
            .eq("email", email)
            .eq("chat_id", chat_id)
            .execute()
        )
        data = data[1]

        # TODO: more check
        if len(data) == 0:
            return [], []

        return json.loads(data[0]["message_history"]), convert_json_to_gemini_history(
            json.loads(data[0]["gemini_history"])
        )


def test_db():
    db = Database(USER_TABLE_NAME, CHAT_TABLE_NAME)
    db.insert_user("sankalp1@gmail.com", "sankalp1", "sankalp1")
    db.insert_user("sankalp2@gmail.com", "sankalp2", "sankalp2")

    exist, username = db.check_email_password("sankalp1@gmail.com", "sankalp1")
    assert exist
    assert username == "sankalp1"

    exist, username = db.check_email_password("sankalp2@gmail.com", "sankalp2")
    assert exist
    assert username == "sankalp2"

    exist, username = db.check_email_password("sankalp99@gmail.com", "sankalp99")
    assert not exist
    assert username is None

    assert db.username_exisits("sankalp1")
    assert not db.username_exisits("sankalp3")

    assert db.email_exisits("sankalp1@gmail.com")
    assert not db.email_exisits("sankalp3@gmail.com")

class SupabaseHandler:
    def __init__(self, url: str, key: str, table_name: str):
        self.supabase: Client = create_client(url, key)
        self.table_name = table_name

    def insert_value(self, record_id: int, text_value: str):
        data = {
            'id': record_id,
            'text': text_value
        }
        fetch_data = self.fetch_value(record_id)
        if not fetch_data:
            try:
                response = self.supabase.table(self.table_name).insert(data).execute()
            except Exception as e:
                raise Exception(e)
            return response.data
        else:
            print("Already there ", fetch_data)


    def fetch_value(self, record_id: int):
        try:
            response = self.supabase.table(self.table_name).select("*").eq('id', record_id).execute()
        except Exception as e:
            raise Exception(e)
        # print(response)
        if response.data:
            return response.data[0]
        else:
            return None


def test_supabase():
    db = SupabaseDatabase(USER_TABLE_NAME, CHAT_TABLE_NAME)
    # db.insert_user("sankalp1@gmail.com", "sankalp1", "sankalp1")
    # db.insert_user("sankalp2@gmail.com", "sankalp2", "sankalp2")

    exist, username = db.check_email_password("sankalp1@gmail.com", "sankalp1")
    assert exist
    assert username == "sankalp1"

    exist, username = db.check_email_password("sankalp2@gmail.com", "sankalp2")
    assert exist
    assert username == "sankalp2"

    exist, username = db.check_email_password("sankalp99@gmail.com", "sankalp99")
    assert not exist
    assert username is None

    assert db.username_exisits("sankalp1")
    assert not db.username_exisits("sankalp3")

    assert db.email_exisits("sankalp1@gmail.com")
    assert not db.email_exisits("sankalp3@gmail.com")


def main():
    test_db()
    # test_supabase()


if __name__ == "__main__":
    main()
