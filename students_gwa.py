def get_latin_honor(gwa):
    if gwa <= 1.20:
        return "Summa Cum Laude"
    elif gwa <= 1.45:
        return "Magna Cum Laude"
    elif gwa <= 1.75:
        return "Cum Laude"
    else:
        return "No Latin Honor"
    
def process_student_gwa():
    filename = input("Enter the name of the input file: ")

    students = []

    try:
        with open(filename, "r") as file:

            for line_num, line in enumerate(file, 1):
                line = line.strip()

                if not line:
                    continue

                parts = line.split()

                if len(parts) < 2:
                    print(
                        f"Warning: Invalid format "
                        f"on line {line_num}"
                    )
                    continue