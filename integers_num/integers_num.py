def process_integers():
    input_file = "integers.txt"
    even_output_file = "double.txt"
    odd_output_file = "triple.txt"

    try:
        with open(input_file, "r") as file:
            # Read all integers (handles spaces or new lines)
            numbers = []
            for line in file:
                parts = line.strip().split()
                for part in parts:
                    numbers.append(int(part))

        if len(numbers) != 20:
            print(f"Warning: Expected 20 integers, found {len(numbers)}")

        even_results = []
        odd_results = []

        for num in numbers:
            if num % 2 == 0:
                # even → square
                even_results.append(num ** 2)
            else:
                # odd → cube
                odd_results.append(num ** 3)
        
         # Write even (squared) numbers
        with open(even_output_file, "w") as file:
            for value in even_results:
                file.write(str(value) + "\n")
