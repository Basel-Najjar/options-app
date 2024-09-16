from tastytrade import Session
import getpass
import os
import json
from datetime import datetime, timedelta


class Auth:
    def __init__(self):
        self.secrets_folder_path = os.path.join(os.getcwd(), "secrets")
        self.now = datetime.today()
        self.load_username()
        self.load_and_validate_token()

    def login(self):
        if self.valid_token:
            print("Logging in with remember Token.")
            try:
                self.token_login()
            except Exception as e:
                print("Failed to login with Token.")
                self.password_login()

        elif not self.valid_token:
            self.password_login()

        print(f"Valid session: {self.session.validate()}")

    def token_login(self):
        self.session = Session(self.username, remember_token=self.token)

    def password_login(self):
        password = getpass.getpass(prompt="Enter tastytrade password:")
        self.session = Session(self.username, password, is_test=False, remember_me=True)
        self.save_token()

    def load_username(self):
        with open(os.path.join(self.secrets_folder_path, "username.txt"), "r") as f:
            self.username = f.read()

    def save_token(self):
        contents = {
            "timestamp": self.now.timestamp(),
            "token": self.session.remember_token,
        }
        with open(os.path.join(self.secrets_folder_path, "token.json"), "w+") as f:
            json.dump(contents, f)

    def load_and_validate_token(self):
        with open(os.path.join(self.secrets_folder_path, "token.json"), "r") as f:
            token_contents = json.load(f)
        self.token_contents = token_contents

        if token_contents["timestamp"] > (self.now - timedelta(hours=24)).timestamp():
            self.token = token_contents["token"]
            self.valid_token = True
        else:
            self.valid_token = False
