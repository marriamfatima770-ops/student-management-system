
import json
import os

FILE_NAME = "students.json"


# Load student records
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save student records
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Add a student
def add_student(students):
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")

    try:
        age = int(input("Enter Student Age: "))
    except ValueError:
        print("Please enter a valid age!")
        return

    department = input("Enter Department: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "department": department
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")


# View students
def view_students(students):
    if not students:
        print("No student records found!")
        return

    for student in students:
        print("\n----------------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Department:", student["department"])


# Search student
def search_student(students):
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print(student)
            return

    print("Student not found!")


# Update student
def update_student(students):
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            print("Leave a field blank to keep its current value.")

            name = input("Enter new name: ")
            age = input("Enter new age: ")
            department = input("Enter new department: ")

            if name.strip():
                student["name"] = name

            if age.strip():
                try:
                    student["age"] = int(age)
                except ValueError:
                    print("Invalid age. Keeping old age.")
                    return

            if department.strip():
                student["department"] = department

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found!")


# Delete student
def delete_student(students):
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found!")


# Main program
def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
