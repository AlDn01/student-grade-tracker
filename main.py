"""
Student Grade Tracker - CLI Application

This file is Yusuf's part.
It handles the menu, user input, and the main system flow.
"""

from grade_tracker import GradeTracker


def show_menu():
    """
    Display the main menu options.
    """
    print("\n===== Student Grade Tracker =====")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Update student grades")
    print("4. Delete a student record")
    print("5. Save and exit")


def get_grades_from_user():
    """
    Ask the user to enter grades and return them as a list.

    The user should enter grades separated by commas.
    Example: 90, 85, 77
    """
    while True:
        grades_input = input("Enter grades separated by commas: ")

        try:
            grades = []

            for grade in grades_input.split(","):
                grade = grade.strip()

                if grade == "":
                    continue

                grade_number = float(grade)

                if grade_number < 0 or grade_number > 100:
                    print("Grades must be between 0 and 100.")
                    break

                grades.append(grade_number)
            else:
                return grades

        except ValueError:
            print("Invalid grade. Please enter numbers only.")


def add_student_flow(tracker):
    """
    Handle adding a new student.
    """
    print("\n--- Add New Student ---")

    name = input("Enter student name: ").strip()
    student_id = input("Enter student ID: ").strip()

    if name == "" or student_id == "":
        print("Name and student ID cannot be empty.")
        return

    grades = get_grades_from_user()

    try:
        tracker.add_student(name, student_id, grades)
        print("Student added successfully.")
    except ValueError as error:
        print(error)


def view_students_flow(tracker):
    """
    Show all students and their average grades.
    """
    print("\n--- All Students ---")

    students = tracker.get_all_students()

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("---------------------------")
        print(f"Name: {student.name}")
        print(f"Student ID: {student.student_id}")
        print(f"Grades: {student.grades}")
        print(f"Average Grade: {student.calculate_average():.2f}")


def update_grades_flow(tracker):
    """
    Handle updating grades for an existing student.
    """
    print("\n--- Update Student Grades ---")

    student_id = input("Enter student ID: ").strip()

    if student_id == "":
        print("Student ID cannot be empty.")
        return

    grades = get_grades_from_user()

    try:
        tracker.update_student_grades(student_id, grades)
        print("Grades updated successfully.")
    except ValueError as error:
        print(error)


def delete_student_flow(tracker):
    """
    Handle deleting a student record.
    """
    print("\n--- Delete Student Record ---")

    student_id = input("Enter student ID: ").strip()

    if student_id == "":
        print("Student ID cannot be empty.")
        return

    confirm = input("Are you sure you want to delete this student? (yes/no): ").lower()

    if confirm != "yes":
        print("Delete cancelled.")
        return

    try:
        tracker.delete_student(student_id)
        print("Student deleted successfully.")
    except ValueError as error:
        print(error)


def main():
    """
    Run the main program.

    The program loads saved data when it starts.
    It keeps running until the user chooses to save and exit.
    """
    tracker = GradeTracker("students.csv")

    try:
        tracker.load_from_csv()
        print("Student data loaded successfully.")
    except FileNotFoundError:
        print("No previous data file found. Starting with empty records.")
    except Exception as error:
        print(f"An error occurred while loading data: {error}")

    while True:
        show_menu()
        choice = input("Choose an option from 1 to 5: ").strip()

        if choice == "1":
            add_student_flow(tracker)

        elif choice == "2":
            view_students_flow(tracker)

        elif choice == "3":
            update_grades_flow(tracker)

        elif choice == "4":
            delete_student_flow(tracker)

        elif choice == "5":
            try:
                tracker.save_to_csv()
                print("Data saved successfully.")
                print("Goodbye!")
                break
            except Exception as error:
                print(f"An error occurred while saving data: {error}")

        else:
            print("Invalid choice. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
