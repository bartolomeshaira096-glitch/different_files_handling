import os
from datetime import datetime


def get_user_choice():
    while True:
        choice = input(
            "Are there more lines (y/n)? "
        ).strip().lower()

        if choice in ("y", "n"):
            return choice

        print(
            "Invalid input. Please enter y or n."
        )


def defining_my_life():
    filename = "journal_project/own_life.txt"

    line_count = 0
    word_count = 0

    try:
        with open(filename, "a") as file:

            file.write("MY LIFE JOURNAL\n")
            file.write(
                f"Created: {datetime.now()}\n"
            )
            file.write("-" * 40 + "\n")

            while True:
                line = input(
                    f"Entry {line_count + 1}: "
                ).strip()

                if line:
                    line_count += 1
                    word_count += len(line.split())

                    file.write(
                        f"{line_count}. {line}\n"
                    )

                choice = get_user_choice()

                if choice == "n":
                    break

        print("\nJournal saved successfully!")
        print("-" * 30)

        # Show file location
        print(
            "Saved in:",
            os.path.abspath(filename)
        )

        print(
            f"Total lines written: {line_count}"
        )
        print(
            f"Total words written: {word_count}"
        )

    except Exception as error:
        print(
            f"An error occurred: {error}"
        )


if __name__ == "__main__":
    defining_my_life()