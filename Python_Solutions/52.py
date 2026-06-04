import json

students = {}


def add_grade(student, grade):

    if 0 <= grade <= 100:

        if student not in students:
            students[student] = []

        students[student].append(grade)

    else:
        print("Invalid grade. Grade must be between 0 and 100.")


def calculate_gpa(student):

    if student in students and len(students[student]) > 0:
        return sum(students[student]) / len(students[student])

    return 0


def save_data():

    with open("grades.json", "w") as file:
        json.dump(students, file, indent=4)


def load_data():

    global students

    try:
        with open("grades.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        print("No saved data found.")


def class_average():

    all_grades = []

    for grades in students.values():
        all_grades.extend(grades)

    if len(all_grades) > 0:
        return sum(all_grades) / len(all_grades)

    return 0


add_grade("Divya", 95)
add_grade("Rahul", 80)
add_grade("Divya", 88)
add_grade("Sneha", 91)
add_grade("Rahul", 76)
add_grade("Arun", 105)

save_data()

load_data()

print("----- Student GPA -----")

for student in students:
    print(f"{student}: {calculate_gpa(student):.2f}")

print(f"\nClass Average: {class_average():.2f}")