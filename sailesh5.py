"""Evaluate a student's marks, attendance, grade, and exam eligibility."""


def get_number(prompt, minimum=0, maximum=100):
    """Read a number within the inclusive range."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if minimum <= value <= maximum:
            return value

        print(f"Please enter a value between {minimum} and {maximum}.")


def get_positive_integer(prompt):
    """Read a positive whole number."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if value > 0:
            return value

        print("Please enter a number greater than zero.")


def calculate_attendance_percentage(total_classes, attended_classes):
    """Return attendance as a percentage."""
    return attended_classes / total_classes * 100


def get_grade(marks):
    """Assign a grade using the student's marks."""
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"


name = input("Enter the student's name: ").strip()
roll_number = input("Enter the student's roll number: ").strip()
marks = get_number("Enter marks (0-100): ")

total_classes = get_positive_integer("Enter total classes conducted: ")
while True:
    attended_classes = get_positive_integer("Enter classes attended: ")
    if attended_classes <= total_classes:
        break
    print("Classes attended cannot exceed classes conducted.")

attendance_percentage = calculate_attendance_percentage(
    total_classes, attended_classes
)

# The calculated percentage is guaranteed to be between 0 and 100.
if marks >= 40:
    result = "Passed"
else:
    result = "Failed"

if attendance_percentage >= 75:
    attendance_status = "Satisfactory"
else:
    attendance_status = "Insufficient"

if attendance_percentage >= 75 and marks >= 40:
    examination_eligibility = "Eligible"
else:
    examination_eligibility = "Not eligible"

print("\n--- Student Report ---")
print(f"Name: {name}")
print(f"Roll number: {roll_number}")
print(f"Marks: {marks:g}")
print(f"Result: {result}")
print(f"Grade: {get_grade(marks)}")
print(f"Attendance: {attendance_percentage:.2f}%")
print(f"Attendance status: {attendance_status}")
print(f"Examination eligibility: {examination_eligibility}")
