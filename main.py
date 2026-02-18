students = {}  # stores all students

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    students[student_id] = {"name": name, "grades": {}}
    print(f"Student {name} added!")

def add_grade():
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Student not found!")
        return
    subject = input("Enter subject: ")
    grade = input("Enter grade: ")
    students[student_id]["grades"][subject] = grade
    print(f"Grade added for {students[student_id]['name']}")

def view_student():
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Student not found!")
        return
    student = students[student_id]
    print(f"Name: {student['name']}")
    print("Grades:")
    for subject, grade in student["grades"].items():
        print(f"  {subject}: {grade}")

def view_all_students():
    for student_id, student in students.items():
        print(f"{student_id} - {student['name']}")

def main():
    while True:
        print("\n1. Add student")
        print("2. Add grade")
        print("3. View student")
        print("4. View all students")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            view_student()
        elif choice == "4":
            view_all_students()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
