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
    filename= input("Enter the name of the input file: ")

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
                try:
                    student_name = " ".join(parts[:-1])
                    gwa = float(parts[-1])

                    students.append(
                        {
                            "name": student_name,
                            "gwa": gwa
                        }
                    )

                except ValueError:
                    print(
                        f"Warning: Invalid GWA "
                        f"on line {line_num}"
                    )
        if not students:
            print("No valid student data found.")
            return

        # Sort students by GWA (lower is better)
        students.sort(
            key=lambda student: student["gwa"]
        )

        # Highest GWA student
        top_student = students[0]

        print("\n" + "=" * 45)
        print(" STUDENT WITH HIGHEST GWA ")
        print("=" * 45)

        print(f"Name  : {top_student['name']}")
        print(f"GWA   : {top_student['gwa']:.2f}")
        print(
            f"Honor : "
            f"{get_latin_honor(top_student['gwa'])}"
        )

        # Top 3 Dean's Listers
        print("\nTOP 3 DEAN'S LISTERS")
        print("-" * 45)

        for rank, student in enumerate(
            students[:3],
            start=1
        ):
            print(
                f"{rank}. "
                f"{student['name']} - "
                f"{student['gwa']:.2f} "
                f"({get_latin_honor(student['gwa'])})"
            )

            # Class Statistics
        total_gwa = sum(
            student["gwa"]
            for student in students
        )

        average_gwa = (
            total_gwa / len(students)
        )

        print("\nCLASS STATISTICS")
        print("-" * 45)
        print(
            f"Number of Students : "
            f"{len(students)}"
        )
        print(
            f"Class Average GWA  : "
            f"{average_gwa:.2f}"
        )

         # Bonus Ranking Leaderboard
        print("\nCLASS RANKING")
        print("-" * 45)

        for rank, student in enumerate(
            students,
            start=1
        ):
            print(
                f"{rank:>2}. "
                f"{student['name']:<20} "
                f"{student['gwa']:.2f}"
            )

    except FileNotFoundError:
        print(
            f"Error: File '{filename}' "
            f"not found."
        )

    except Exception as error:
        print(
            f"An error occurred: "
            f"{error}"
        )


if __name__ == "__main__":
    process_student_gwa()


