"""
letter_grades.py
@author: Jackie Johnson-Dallas
This script will create average grade for a student after entering a desired
amount of grades.
"""


class ClassAverage:
    """This class will represent an average of grades."""

    def __init__(self, assignments):
        """Initialize with properties for average"""
        self.assignments = assignments

    def _convert_to_letter(self, grade):
        """Helper method to convert to letter grade"""

        if grade >= 90:
            return 'A'
        elif grade >= 80:
            return 'B'
        elif grade >= 70:
            return 'C'
        elif grade >= 60:
            return 'D'
        else:
            return 'F'

    def get_average(self):
        """Get average of grades."""
        total_points = 0
        for grade in self.assignments.values():
            total_points += grade
        average = total_points / len(self.assignments.values())
        formatted_average = average.__format__('.2f')
        final_letter_grade = self._convert_to_letter(int(average))
        report = f"""
            Average for all scores entered
            Final Average:          {formatted_average}
            Final Letter Grade:     {final_letter_grade}
        """
        print(report)

    def show_grades(self):
        """Print assignments and grades"""
        for assignment, grade in self.assignments.items():

            report = f"""
            Assignment Description: {assignment}
            Score: {grade}
            Letter Grade: {self._convert_to_letter(grade)}
            """
            print(report)


while True:

    total_grades = int(input("How many grades do you to average? "))

    if total_grades > 0:
        new_student = {}
        for _ in range(total_grades):
            valid_score = False
            assignment_detail = input(
                "\nPlease enter the assignment description (ex. Test1): ")
            while valid_score is False:
                assignment_score = int(
                    input(f"Please enter the score for {assignment_detail}: "))
                if assignment_score >= 0 and assignment_score <= 100:
                    new_student[assignment_detail] = assignment_score
                    valid_score = True
                else:
                    print("Assignment score has to be between 0 and 100.\n")

        new_student_average = ClassAverage(new_student)
        print("\n")
        assignments = new_student_average.assignments
        new_student_average.show_grades()
        new_student_average.get_average()
        break
    else:
        print("The amount of grades you want to enter have to be > 0.\n")
