from data import student_list
from file_manager import load_students, view_file, clear_data, delete_file
from operations import (add_student, display_students, search_student, update_student, delete_student)

def main_menu():

    while True:

        print("""
===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. Display All Students
3. Search Student
4. Update Student
5. Delete Student
6. View File
7. Clear All Data
8. Delete Student File
9. Exit
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            view_file()

        elif choice == "7":
            clear_data()

        elif choice == "8":
            delete_file()

        elif choice == "9":
            print("Exiting Student Management System...")
            break

        else:
            print("\"INVALID CHOICE\"")

load_students()
main_menu()