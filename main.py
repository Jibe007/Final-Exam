# main.py
from game import Game
from user import get_user_login


def main():
    print("Welcome to 'Guess the Number'!")

    # Handle user authentication
    username = get_user_login()

    # Start the game
    game = Game(username)
    game.play()


if __name__ == "__main__":
    main()
