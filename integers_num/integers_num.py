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