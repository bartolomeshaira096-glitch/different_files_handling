class NumberSeparator:

    def __init__(self):
        self.input_filename = "numbers.txt"
        self.even_filename = "even.txt"
        self.odd_filename = "odd.txt"

    def separate_numbers(self):
        with open(
            self.input_filename,
            "r"
        ) as file:

            number_list = [
                int(line.strip())
                for line in file
            ]

        even_number_list = []
        odd_number_list = []

        for current_number in number_list:

            if current_number % 2 == 0:
                even_number_list.append(
                    current_number
                )
            else:
                odd_number_list.append(
                    current_number
                )

        with open(
            self.even_filename,
            "w"
        ) as even_file:

            for even_number in even_number_list:
                even_file.write(
                    f"{even_number}\n"
                )
        # Write even numbers to even.txt
        with open("even.txt", "w") as even_file:
            for num in even_numbers:
                even_file.write(str(num) + "\n")

        # Write odd numbers to odd.txt
        with open("odd.txt", "w") as odd_file:
            for num in odd_numbers:
                odd_file.write(str(num) + "\n")

        print("Done! Numbers have been separated into even.txt and odd.txt.")

    except FileNotFoundError:
        print("Error: numbers.txt file not found.")
    except ValueError:
        print("Error: Make sure all lines in numbers.txt are integers.")

# Run the function
separate_numbers()

#Fixed directory path issues