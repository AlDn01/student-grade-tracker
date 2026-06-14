# student-grade-tracker
# Student Grade Tracker (CLI Application)

## Project Description

The Student Grade Tracker is a Python command-line application designed to manage student records with persistent storage. It allows users to add students, view all records, update grades, delete students, and automatically save/load data using a CSV file.

The project demonstrates object-oriented programming, clean code practices, input validation, exception handling, and file-based data persistence using Python’s built-in `csv` module.

---

## Features

* Add a new student (name, student ID, list of grades)
* View all students and their average grade
* Update grades for an existing student
* Delete a student record
* Save data to CSV and reload automatically on startup
* Input validation for names, IDs, and grades
* Robust error handling

---

## Project Structure

```
student-grade-tracker/
│
├── main.py              # CLI interface and user interaction
├── grade_tracker.py     # Core logic (Student & GradeTracker classes)
├── students.csv        # Persistent storage file (auto-generated)
└── README.md           # Project documentation
```

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/USERNAME/student-grade-tracker.git
cd student-grade-tracker
```

### 2. Run the program

```bash
python main.py
```

Make sure Python 3 is installed on your system.

---

## Requirements

* Python 3.x
* No external libraries required

---

## System Design

The application is structured into three main layers:

* **User Interface (main.py):** Handles menus and user input
* **Core Logic (grade_tracker.py):** Manages students using OOP classes
* **Data Storage:** CSV file for persistent storage

---

## Team Contributions

### Asem — Core Logic & Data Processing

* Implemented `Student` and `GradeTracker` classes
* Built CSV read/write functionality
* Implemented CRUD operations:

  * Add student (with duplicate ID protection)
  * Find student
  * Update grades
  * Delete student
* Handled file loading errors and data validation
* Ensured safe data persistence using `csv` module

---

### Yusuf — System Flow & Application Logic

* Designed CLI menu system
* Implemented user interaction flows:

  * Add student flow
  * View students flow
  * Update grades flow
  * Delete student flow
* Connected UI layer with backend logic
* Ensured smooth application workflow

---

### Allaa — Code Quality & Integration

* Refactored and cleaned `main.py`
* Implemented input validation:

  * Full name validation (first + last name)
  * Student ID format validation
  * Grade range validation (0–100)
* Improved error messages and user experience
* Ensured proper integration between all modules
* Wrote and structured this README file
* Verified full system functionality

---

## Notes

* Data is automatically saved in `students.csv`
* Data is loaded automatically when the program starts
* Invalid inputs are safely handled to prevent crashes

---

## Future Improvements

* Add GUI version (Tkinter or web app)
* Add authentication system for multiple users
* Export reports (PDF/Excel)
* GPA calculation system instead of simple averages
