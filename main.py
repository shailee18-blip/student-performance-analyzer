
def calculate_total(marks):
    total = 0

    for mark in marks:
        total = total + mark

    return total


def calculate_avg(marks):
    total = calculate_total(marks)
    average = total / len(marks)
    return average


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "Fail"


def find_highest(marks):
    highest = marks[0]

    for mark in marks:
        if mark > highest:
            highest = mark

    return highest


def find_lowest(marks):
    lowest = marks[0]

    for mark in marks:
        if mark < lowest:
            lowest = mark

    return lowest


def check_pass_fail(marks):
    for mark in marks:
        if mark < 35:
            return "Fail"

    return "Pass"


# Student data
students = [
    {"name": "Aarav", "marks": [85, 90, 78, 92, 88]},
    {"name": "Diya", "marks": [65, 72, 81, 59, 75]},
    {"name": "Kabir", "marks": [85, 90, 28, 92, 88]}
]


# Generate individual student reports
for student in students:
    name = student["name"]
    marks = student["marks"]

    total = calculate_total(marks)
    average = calculate_avg(marks)
    grade = calculate_grade(average)
    highest = find_highest(marks)
    lowest = find_lowest(marks)
    result = check_pass_fail(marks)

    print("\n--------------------")
    print("Student:", name)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Result:", result)


# Find the class topper
topper = students[0]

for student in students:
    current_average = calculate_avg(student["marks"])
    topper_average = calculate_avg(topper["marks"])

    if current_average > topper_average:
        topper = student


print("\n===== CLASS TOPPER =====")
print("Name:", topper["name"])
print("Average:", calculate_avg(topper["marks"]))

# Class summary
total_students = len(students)
passed_students = 0
failed_students = 0
total_class_marks = 0

for student in students:
    marks = student["marks"]
    result = check_pass_fail(marks)

    total_class_marks += calculate_total(marks)

    if result == "Pass":
        passed_students += 1
    else:
        failed_students += 1

class_average = total_class_marks / (
    total_students * len(students[0]["marks"])
)

print("\n===== CLASS SUMMARY =====")
print("Total students:", total_students)
print("Students passed:", passed_students)
print("Students failed:", failed_students)
print("Class average:", round(class_average, 2))
