# user.py
from file_manager import FileManager


class UserManager:
    def __init__(self):
        self.user_file = "data/accounts.txt"
        self.current_user = None

    def login(self):
        username = input("Enter your username: ")
        if FileManager.check_user(username):
            print("Login successful!")
            self.current_user = username
            return True
        print("No such user found.")
        return False

    def register(self):
        username = input("Enter a username to register: ")
        FileManager.register_user(username)
        print("Account created! You can now log in.")


def get_user_login():
    user_manager = UserManager()
    if not user_manager.login():
        user_manager.register()
    return user_manager.current_user
