from integers_num.integers_num import IntegerProcessor
from journal_project.my_journal import JournalManager
from odd_and_even_separator.odd_even_separator import NumberSeparator
from student_gwa_project.students_gwa import StudentGWAManager

if __name__ == "__main__":
    
    integer_processor = IntegerProcessor()
    integer_processor.process_numbers()
    
    journal_manager = JournalManager()
    journal_manager.create_journal()
    
    number_separator = NumberSeparator()
    number_separator.separate_numbers()
    
    student_gwa_manager = StudentGWAManager()
    student_gwa_manager.process_student_records()

    print("PROGRAM STARTED")