name = input("Enter student name: ")

math = float(input("Enter Mathematics marks: "))
python = float(input("Enter Python marks: "))
english = float(input("Enter English marks: "))
computer = float(input("Enter Computer Science marks: "))
statistics = float(input("Enter Statistics marks: "))

total = math + python + english + computer + statistics
percentage = total / 5

if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- Student Result -----")
print("Student:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)