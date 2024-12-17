# file_manager.py
import os


class FileManager:
    @staticmethod
    def check_user(username):
        """Check if username exists in the accounts file."""
        if not os.path.exists("data/accounts.txt"):
            return False
        with open("data/accounts.txt", "r") as file:
            for line in file:
                if line.strip() == username:
                    return True
        return False

    @staticmethod
    def register_user(username):
        """Register a new user by saving their username to the file."""
        with open("data/accounts.txt", "a") as file:
            file.write(f"{username}\n")

    @staticmethod
    def save_game_attempts(username, attempts):
        """Save the number of attempts with the username in stats.txt."""
        if not os.path.exists("data/stats.txt"):
            with open("data/stats.txt", "w") as file:
                file.write(f"Username: {username}, Attempts: {attempts}\n")
        else:
            with open("data/stats.txt", "a") as file:
                file.write(f"Username: {username}, Attempts: {attempts}\n")
