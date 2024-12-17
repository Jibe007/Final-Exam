# utils.py
def read_translations():
    """Mock function to return simple translations."""
    return {
        "welcome_game": "Welcome to the Guess the Number Game! You have 5 lives.",
        "prompt_guess": "Guess the number between 1 and 40: ",
        "hint_higher": "Try a higher number.",
        "hint_lower": "Try a lower number.",
        "error_invalid_input": "Invalid input. Please enter a number.",
        "correct_guess": "Congratulations! You guessed the correct number in {} attempts."
    }
