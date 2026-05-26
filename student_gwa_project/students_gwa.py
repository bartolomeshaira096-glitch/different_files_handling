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

        student_record_list.sort(
            key=lambda student_record:
            student_record["student_gwa"]
        )

        highest_student = (
            student_record_list[0]
        )

        print(
            f"\nHighest GWA: "
            f"{highest_student['student_name']}"
        )

        print(
            f"GWA: "
            f"{highest_student['student_gwa']}"
        )

        print(
            f"Honor: "
            f"{self.get_latin_honor(highest_student['student_gwa'])}"
        )