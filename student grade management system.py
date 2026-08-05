# ---------------- Student Class ----------------
class Student:
    def __init__(self, student_id, name):
        self._student_id = student_id
        self._name = name

    def display(self):
        print("\nStudent ID :", self._student_id)
        print("Student Name :", self._name)


# ---------------- Subject Class ----------------
class Subject:
    def __init__(self):
        self._subjects = {}

    def add_subject(self):
        name = input("Enter Subject Name: ")
        marks = int(input("Enter Marks: "))
        self._subjects[name] = marks
        print("Subject Added Successfully!")

    def view_subjects(self):
        if len(self._subjects) == 0:
            print("No subjects added.")
        else:
            print("\nSubjects and Marks")
            for subject, marks in self._subjects.items():
                print(subject, ":", marks)

    def get_marks(self):
        return self._subjects


# ---------------- Grade Calculator Class ----------------
class GradeCalculator:
    def calculate_average(self, marks):
        if len(marks) == 0:
            return 0
        return sum(marks.values()) / len(marks)

    def calculate_grade(self, average):
        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "Fail"


# ---------------- Report Card Class ----------------
class ReportCard:
    def __init__(self, student, subject, calculator):
        self.student = student
        self.subject = subject
        self.calculator = calculator

    def display_report(self):
        marks = self.subject.get_marks()

        if len(marks) == 0:
            print("No subjects available.")
            return

        average = self.calculator.calculate_average(marks)
        grade = self.calculator.calculate_grade(average)

        print("\n========== REPORT CARD ==========")
        self.student.display()

        print("\nMarks")
        for subject, mark in marks.items():
            print(subject, ":", mark)

        print("\nAverage :", round(average, 2))
        print("Grade :", grade)
        print("=================================")


# ---------------- Main Program ----------------

student_id = int(input("Enter Student ID: "))
name = input("Enter Student Name: ")

student = Student(student_id, name)
subjects = Subject()
calculator = GradeCalculator()
report = ReportCard(student, subjects, calculator)

while True:
    print("\n====== STUDENT GRADE MANAGEMENT ======")
    print("1. Add Subject Marks")
    print("2. View Subjects")
    print("3. Display Report Card")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        subjects.add_subject()

    elif choice == 2:
        subjects.view_subjects()

    elif choice == 3:
        report.display_report()

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")