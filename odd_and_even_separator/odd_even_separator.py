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
        
        with open(
            self.odd_filename,
            "w"
        ) as odd_file:

            for odd_number in odd_number_list:
                odd_file.write(
                    f"{odd_number}\n"
                )

        print(
            "Numbers successfully separated."
        )