# Student Management System

A Python-based Student Management System developed as a learning project to practice object-oriented programming, file handling, validation, modular programming, and CRUD operations.

## Current Version

**Version 2.0**

Version 1 is preserved in the `V1` folder to show the development and learning progression of the project.

---

## Version 1.0

Version 1 was developed as a single-file project using Jupyter Notebook and Python.

### Main Features

- Add students
- Display all students
- Search students
- Update student information
- Delete students
- Input validation
- File handling using `students.txt`
- Object-Oriented Programming using a `Student` class
- Automatic loading of saved student data
- Handling of invalid/corrupted records

V1 is available inside:

```text
V1/
```

---

## Version 2.0

Version 2 improves the original project by converting it into a modular multi-file Python application.

### Main Features

- Add Student
- Display All Students
- Search Student
- Update Student
- Delete Student
- View saved file
- Clear all student data
- Delete student data file
- Input validation
- Persistent file storage
- Automatic loading of saved data
- Invalid/corrupted record handling
- Duplicate record protection

### Student Identification

In V2, a student is uniquely identified using:

```text
Semester + Student ID
```

This means the same Student ID may exist in different semesters, but the same Student ID cannot be repeated within the same semester.

---

## Project Structure

```text
student-management-system/
│
├── V1/
│   ├── README.md
│   ├── student_management_system.ipynb
│   └── student_management_system.py
│
├── V2/
│   ├── README.md
│   ├── main.py
│   ├── student.py
│   ├── constants.py
│   ├── data.py
│   ├── operations.py
│   └── file_manager.py
│
└── README.md
```

### V2 File Responsibilities

- `main.py` — Main menu and program entry point
- `student.py` — Student class and student-related methods
- `constants.py` — Valid grades and available programs
- `data.py` — Shared student list
- `operations.py` — Add, display, search, update, and delete operations
- `file_manager.py` — Saving, loading, viewing, clearing, and deleting student data

---

## Data Storage

Student data is stored in:

```text
students.txt
```

The file is automatically created when student data is saved.

V2 uses a project-based file path so the data file remains associated with the project folder instead of depending on the current working directory.

---

## Technologies Used

- Python
- Object-Oriented Programming
- File Handling
- Exception Handling
- Input Validation
- Modular Programming

---

## How to Run V2

1. Open the `V2` folder.
2. Run:

```bash
python main.py
```

3. Use the menu to manage student records.

---

## Learning Progression

```text
V1
Single-file Python/Jupyter project
        ↓
V2
Modular multi-file Python application
```

The purpose of this project is to improve Python programming skills by gradually upgrading the same application with better structure, validation, and design.
