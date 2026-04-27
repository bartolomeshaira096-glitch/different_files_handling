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

def defining_my_life():
    filename = "own_life.txt"

    line_count = 0
    word_count = 0

    try:
        with open(filename, "w") as file:

            file.write(
                "MY LIFE JOURNAL\n"
            )
            file.write(
                f"Created: "
                f"{datetime.now()}\n"
            )
            file.write(
                "-" * 40 + "\n"
            )