"""
grade_tracker.py
Contains the Student and GradeTracker classes for the Student Grade Tracker application.
"""

import csv
import os


class Student:
    """
    Represents a single student with a name, student ID, and a list of grades.

    Attributes:
        name (str): The full name of the student.
        student_id (str): A unique identifier for the student.
        grades (list[float]): A list of numeric grades between 0 and 100.
    """

    def __init__(self, name, student_id, grades=None):
        """
        Initialize a Student instance.

        Args:
            name (str): The student's full name.
            student_id (str): The student's unique ID.
            grades (list[float], optional): Initial list of grades. Defaults to empty list.
        """
        self.name = name
        self.student_id = student_id
        self.grades = grades if grades is not None else []

    def calculate_average(self):
        """
        Calculate the average of the student's grades.

        Returns:
            float: The average grade, or 0.0 if there are no grades.
        """
        if len(self.grades) == 0:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        """
        Return a human-readable string representation of the student.

        Returns:
            str: Formatted student info including name, ID, grades, and average.
        """
        return (
            f"Student(name={self.name}, "
            f"id={self.student_id}, "
            f"grades={self.grades}, "
            f"average={self.calculate_average():.2f})"
        )


class GradeTracker:
    """
    Manages a collection of Student objects and handles CSV-based persistence.

    Attributes:
        filepath (str): Path to the CSV file used for saving and loading data.
        students (list[Student]): In-memory list of all students.
    """

    def __init__(self, filepath):
        """
        Initialize the GradeTracker with a given CSV file path.

        Args:
            filepath (str): Path to the CSV file for persistent storage.
        """
        self.filepath = filepath
        self.students = []

    def add_student(self, name, student_id, grades):
        """
        Add a new student to the tracker.

        Args:
            name (str): The student's full name.
            student_id (str): The student's unique ID.
            grades (list[float]): List of grades for the student.

        Raises:
            ValueError: If a student with the same ID already exists.
        """
        for student in self.students:
            if student.student_id == student_id:
                raise ValueError(f"A student with ID '{student_id}' already exists.")
        new_student = Student(name, student_id, grades)
        self.students.append(new_student)

    def get_all_students(self):
        """
        Return the list of all students.

        Returns:
            list[Student]: All students currently tracked.
        """
        return self.students

    def find_student(self, student_id):
        """
        Find and return a student by their ID.

        Args:
            student_id (str): The ID of the student to look up.

        Returns:
            Student or None: The matching Student object, or None if not found.
        """
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def update_student_grades(self, student_id, grades):
        """
        Replace the grades of an existing student.

        Args:
            student_id (str): The ID of the student to update.
            grades (list[float]): The new list of grades.

        Raises:
            ValueError: If no student with the given ID is found.
        """
        student = self.find_student(student_id)
        if student is None:
            raise ValueError(f"No student found with ID '{student_id}'.")
        student.grades = grades

    def delete_student(self, student_id):
        """
        Remove a student record from the tracker.

        Args:
            student_id (str): The ID of the student to delete.

        Raises:
            ValueError: If no student with the given ID is found.
        """
        student = self.find_student(student_id)
        if student is None:
            raise ValueError(f"No student found with ID '{student_id}'.")
        self.students.remove(student)

    def save_to_csv(self):
        """
        Save all student records to the CSV file.

        The CSV has three columns: name, student_id, grades.
        Grades are stored as a semicolon-separated string (e.g. "90.0;85.0;77.0").

        Raises:
            IOError: If the file cannot be written.
        """
        with open(self.filepath, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["name", "student_id", "grades"])
            for student in self.students:
                grades_str = ";".join(str(g) for g in student.grades)
                writer.writerow([student.name, student.student_id, grades_str])

    def load_from_csv(self):
        """
        Load student records from the CSV file into memory.

        Grades are parsed from a semicolon-separated string back into a list of floats.
        Skips any rows with missing or malformed data without crashing.

        Raises:
            FileNotFoundError: If the CSV file does not exist.
        """
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File '{self.filepath}' not found.")

        self.students = []
        with open(self.filepath, mode="r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                try:
                    name = row["name"].strip()
                    student_id = row["student_id"].strip()
                    grades_raw = row["grades"].strip()

                    if name == "" or student_id == "":
                        continue

                    if grades_raw == "":
                        grades = []
                    else:
                        grades = [float(g) for g in grades_raw.split(";")]

                    self.students.append(Student(name, student_id, grades))
                except (KeyError, ValueError):
                    continue
