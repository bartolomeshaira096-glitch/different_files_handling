class IntegerProcessor:

    def __init__(self):
        self.input_file = "integers_num/integers.txt"
        self.even_output_file = "integers_num/double.txt"
        self.odd_output_file = "integers_num/triple.txt"

    def read_numbers(self):
        integer_list = []

        with open(self.input_file, "r") as file:
            for line in file:
                values = line.strip().split()

                for value in values:
                    integer_list.append(int(value))

        return integer_list

    def process_numbers(self):
        integer_list = self.read_numbers()

        even_square_results = []
        odd_cube_results = []

        for current_number in integer_list:
            if current_number % 2 == 0:
                even_square_results.append(
                    current_number ** 2
                )
            else:
                odd_cube_results.append(
                    current_number ** 3
                )

        with open(self.even_output_file, "w") as file:
            for result in even_square_results:
                file.write(f"{result}\n")

        with open(self.odd_output_file, "w") as file:
            for result in odd_cube_results:
                file.write(f"{result}\n")

        print("Integer processing complete!")