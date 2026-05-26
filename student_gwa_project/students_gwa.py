class StudentGWAManager:

    def get_latin_honor(
    self,
    student_gwa
):
    if student_gwa <= 1.20:
        return "Summa Cum Laude"

    if student_gwa <= 1.45:
        return "Magna Cum Laude"

    if student_gwa <= 1.75:
        return "Cum Laude"

    return "No Latin Honor"

    def process_student_records(self):

        input_filename = input(
            "Enter input filename: "
        )

        student_record_list = []

        with open(
            input_filename,
            "r"
        ) as file:

            for line_number, line in enumerate(
                file,
                start=1
            ):

                cleaned_line = line.strip()

                if not cleaned_line:
                    continue

                separated_values = (
                    cleaned_line.split()
                )

                student_name = " ".join(
                    separated_values[:-1]
                )

                student_gwa = float(
                    separated_values[-1]
                )

                student_record_list.append(
                    {
                        "student_name":
                        student_name,

                        "student_gwa":
                        student_gwa
                    }
                )

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


