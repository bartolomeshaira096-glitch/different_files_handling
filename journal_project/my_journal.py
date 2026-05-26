import os
from datetime import datetime


class JournalManager:

    def get_user_choice(self):
        while True:
            user_choice = input(
                "Are there more lines (y/n)? "
            ).lower()

            if user_choice in ["y", "n"]:
                return user_choice

            print("Invalid input.")


def create_journal(self):
        journal_filename = (
            "journal_project/own_life.txt"
        )

        total_line_count = 0
        total_word_count = 0

        with open(journal_filename, "a") as file:

            file.write("MY LIFE JOURNAL\n")
            file.write(
                f"Created: {datetime.now()}\n"
            )
            file.write("-" * 40 + "\n")

            while True:

                journal_entry = input(
                    f"Entry {total_line_count + 1}: "
                ).strip()

                if journal_entry:
                    total_line_count += 1
                    total_word_count += len(
                        journal_entry.split()
                    )

                    file.write(
                        f"{total_line_count}. "
                        f"{journal_entry}\n"
                    )

                if self.get_user_choice() == "n":
                    break

        print(
            os.path.abspath(
                journal_filename
            )
        )

        print(
            f"Lines Written: {total_line_count}"
        )

        print(
            f"Words Written: {total_word_count}"
        )