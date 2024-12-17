# game.py
import random
from utils import read_translations
from file_manager import FileManager


class Game:
    def __init__(self, username):
        self.username = username  # Store the logged-in username
        self.number_to_guess = random.randint(1, 40)  # Adjusted range to 1-40
        self.attempts = 0
        self.lives = 5  # 5 lives for the player
        self.translations = read_translations()

    def play(self):
        print(self.translations["welcome_game"])
        while self.lives > 0:
            try:
                guess = int(input(self.translations["prompt_guess"]))
                self.attempts += 1
                if guess == self.number_to_guess:
                    print(self.translations["correct_guess"].format(self.attempts))
                    # Correctly save the stats with both the username and attempts
                    FileManager.save_game_attempts(self.username, self.attempts)
                    break
                elif guess < self.number_to_guess:
                    print(self.translations["hint_higher"])
                    self.lives -= 1
                    print(f"You lost a life. You now have {self.lives} lives remaining.")
                else:
                    print(self.translations["hint_lower"])
                    self.lives -= 1
                    print(f"You lost a life. You now have {self.lives} lives remaining.")
            except ValueError:
                print(self.translations["error_invalid_input"])

        if self.lives == 0:
            print(f"Out of lives! The number was: {self.number_to_guess}")
