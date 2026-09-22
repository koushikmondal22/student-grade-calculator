name = input("Enter student name: ")

def get_marks(subject):
    while True:
        marks = float(input(f"Enter {subject} marks (0-100): "))

        if 0 <= marks <= 100:
            return marks
        else:
            print("Invalid marks! Please enter a number between 0 and 100.")

math = get_marks("Mathematics")
python = get_marks("Python")
english = get_marks("English")
computer = get_marks("Computer Science")
statistics = get_marks("Statistics")

total = math + python + english + computer + statistics
percentage = total / 5

if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

grade = calculate_grade(percentage)

print("\n----- Student Result -----")
print("Student:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)