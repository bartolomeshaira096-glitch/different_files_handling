from datetime import datetime


def get_user_choice():
    while True:
        choice = input(
            "Are there more lines (y/n)? "
        ).strip().lower()

        if choice in ("y", "n"):
            return choice

        print(
            "Invalid input. "
            "Please enter y or n."
        )