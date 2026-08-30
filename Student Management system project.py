#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## importing os and using in delete file function
import os

# class - the blueprint
class Student:

    def __init__(self, name, age, student_id, course, semester, grade):
        self.__name = name
        self.__age = age
        self.__student_id = student_id
        self.__course = course
        self.__semester = semester
        self.__grade = grade

    # getters
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_id(self):
        return self.__student_id

    def get_course(self):
        return self.__course

    def get_semester(self):
        return self.__semester

    def get_grade(self):
        return self.__grade

    # setters
    def set_name(self, name):
        if name.strip():
            self.__name = name
            return True
        else:
            print("Name cannot be empty")
            return False

    def set_age(self, age):
        if 15 < age < 61:
            self.__age = age
            return True
        else:
            print("Age must be between 16 and 60")
            return False

    def set_id(self, student_id):
        if student_id > 0:
            self.__student_id = student_id
            return True
        else: 
            print("INVALID ID")
            return False

    def set_grade(self, grade):
        grade = grade.upper().strip()
        if grade in valid_grades:
            self.__grade = grade
            return True
        else:
            print("INVALID GRADE")
            return False

    def set_course(self, course):
        if course.strip():
            self.__course = course
            return True
        else:
            print("Course cannot be empty")
            return False

    def set_semester(self, semester):
        if 1 <= semester <= 8:
            self.__semester = semester
            return True
        else:
            print("Semester must be between 1 and 8")
            return False
# class structure ends

# outside class normal coding
student_list = []
valid_grades = ["A+", "A", "B+", "B", "C", "D", "F"]
courses = ["BS Artificial Intelligence","BS Computer Science", "BS Software Engineering",
    "BS Information Technology",
    "BS Data Science",
    "BS Cyber Security",
    "BS Electrical Engineering",
    "BS Electronics Engineering",
    "BS Computer Engineering",
    "BS Telecommunication Engineering",
    "BS Mechanical Engineering",
    "BS Civil Engineering",
    "BS Biomedical Engineering",
    "BS Industrial Engineering",
    "BS Mathematics",
    "BS Physics",
    "BS Business Administration",
    "BS Accounting and Finance",
    "BS Economics",
    "BS English",
    "BS Media Studies",
    "BS Psychology"]

def save_students():
    try:
        with open("students.txt", "w") as file:
            for student in student_list:
                file.write(f"{student.get_name()},{student.get_age()},{student.get_id()},{student.get_course()},{student.get_semester()},{student.get_grade()}\n")

        print("Data Saved Successfully")

    except OSError:
        print("Error: Could not save student data.")

def load_students():
    skipped_records= 0

    try:
        with open("students.txt", "r") as file:
            for line in file:
                data= [item.strip() for item in line.split(",")]
                if len(data)!=6:
                    skipped_records += 1
                    continue
                try:
                    name= data[0]
                    if not name or not all(character.isalpha() or character in " '-" for character in name) or not any(character.isalpha() for character in name):
                        skipped_records += 1
                        continue

                    age= int(data[1])
                    if not (15 < age < 61):
                        skipped_records += 1
                        continue

                    student_id= int(data[2])
                    if student_id <= 0:
                        skipped_records += 1
                        continue

                    id_exists= False
                    for student in student_list:
                        if student.get_id() == student_id:
                            id_exists= True
                            break

                    if id_exists:
                        skipped_records += 1
                        print(f"Warning: Duplicate student ID {student_id} found. Record skipped.")
                        continue

                    course = data[3]
                    if course not in courses:
                        skipped_records += 1
                        continue

                    semester = int(data[4])
                    if not (1 <= semester <= 8):
                        skipped_records += 1
                        continue

                    grade = data[5]
                    if grade not in valid_grades:
                        skipped_records += 1
                        continue

                    student= Student(name, age, student_id, course, semester, grade)
                    student_list.append(student) 

                except ValueError:
                    skipped_records += 1
                    continue

            if not student_list:
                print("No valid saved student data found. Starting with empty data.")

            if skipped_records > 0:
                print(f"{skipped_records} invalid record(s) skipped.")

    except FileNotFoundError:
        print("No student file found. Starting with empty data.")

# current + file data resetter
def clear_data():
    while True:
        choice= input("Are you sure you want to clear all student data? (y/n): ").lower().strip()
        if choice == "y":
            student_list.clear()

            with open("students.txt", "w") as file:
                pass
            print("All student data cleared successfully")
            break

        elif choice == "n":
            print("Data deletion cancelled!")
            break

        else: 
            print("Please enter 'y/n'")

# old saved data + file removal
def delete_file():

    if not os.path.exists("students.txt"):
        print("\"File does not exist\"")
        return

    while True:
        choice= input("Are you sure you want to delete the student file?"
                      "All saved student data will be permanently removed. (y/n): ").lower().strip()

        if choice == "y":
            os.remove("students.txt")
            print("Student file deleted successfully. All saved student data has been removed.")
            break

        elif choice == "n":
            print("File deletion cancelled!")
            break

        else:
            print("Please enter 'y/n'")

# viewing file function
def view_file():
    try:
        with open("students.txt", "r") as file:
            data= file.read()

            if data:
                print(data)
            else:
                print("No Data Found")

    except FileNotFoundError:
        print("File does not exist")

def add_student():

    while True:
        name = input("Enter Name (or 'back' to cancel): ").strip().title()

        if name.lower() == "back":
            return

        # empty name + (all)special case checking other than alphabets '-  + (any) one should be alphabet 
        if name and all(character.isalpha() or character in " '-" for character in name) and any(character.isalpha() for character in name):
            break
        else:
            print("Invalid Name")

    while True:

        try:
            age_input = input("Enter Age (or 'back' to cancel): ").strip()

            if age_input.lower() == "back":
                return

            age = int(age_input)

            if 15 < age < 61:
                break
            else:
                print("Age must be between 16 and 60")

        except ValueError:
            print("\"Enter a valid number\"")

    while True:

        try:
            id_input = input("Enter ID (or 'back' to cancel): ").strip()

            if id_input.lower() == "back":
                return

            st_id= int(id_input)

            id_exists = False

            for student in student_list:
                if student.get_id() == st_id:
                    id_exists = True
                    break

            if st_id > 0 and not id_exists:
                break
            else:
                print("ID Must Be POSITIVE and UNIQUE")

        except ValueError:
            print("\"Enter a valid number\"")

    while True:

        grade = input("Enter Grade (A+, A, B+, B, C, D, F) or 'back' to cancel: ").upper().strip()

        if grade == "BACK":
            return

        if grade in valid_grades:
            break
        else:
            print("INVALID GRADE")

    selected_course_rt= select_course()

    if selected_course_rt is None:
        return

    print(f"Course Selected Successfully - {selected_course_rt}")

    while True:

        try:
            semester_input = input("Enter Semester(1-8) or 'back' to cancel: ").strip()

            if semester_input.lower() == "back":
                return

            semester= int(semester_input)

            if 1 <= semester <= 8:
                break
            else:
                print("Semester must be between 1 and 8")

        except ValueError:
            print("\"Enter a valid number\"")

    student = Student(name, age, st_id, selected_course_rt, semester, grade)
    student_list.append(student)
    save_students()

    print("\"Student Added Successfully\"")


def display_students():

    if not student_list:
        print("NO STUDENT FOUND!")
        return

    print(f"{'ID':<6}{'Name':<15}{'Age':<6}{'Course':<35}{'Sem':<6}{'Grade':<6}")

    for student in student_list:
        print(f"{student.get_id():<6}{student.get_name():<15}{student.get_age():<6}{student.get_course():<35}{student.get_semester():<6}{student.get_grade():<6}")


def display_student(student):

    print(f"""
---STUDENT DETAILS---
Name: {student.get_name()}
Age: {student.get_age()}
ID: {student.get_id()}
Course: {student.get_course()}
Semester: {student.get_semester()}
Grade: {student.get_grade()}
---------------------""")


def search_student():    
    if not student_list:
        print("NO STUDENT AVAILABLE")
        return

    while True:
        try:
            search_input = input("Enter Student ID (or 'back' to cancel): ").strip()

            if search_input.lower() == "back":
                return

            student_id= int(search_input)

            if student_id > 0:
                break
            else:
                print("ID must be positive")

        except ValueError:
            print("\"Enter a valid number\"")

    for student in student_list:

        if student.get_id() == student_id:
            display_student(student)
            break

    else:
        print("Student NOT FOUND!")


def select_course():
    while True:
        print("\n===== AVAILABLE COURSES =====")
        for i, course in enumerate(courses, start=1):
            print(f" {i}. {course}")

        try:
            course_input= input("Enter Course Number (or 'back' to cancel): ").strip()

            if course_input.lower() == "back":
                return None

            course_number = int(course_input)

            if 1 <= course_number <= len(courses):
                selected_course= courses[course_number-1]
                return selected_course
            else:
                print("Invalid Course Selection")

        except ValueError:
            print("Invalid Number")

def update_student():
    if not student_list:
        print("NO STUDENT AVAILABLE")
        return


    while True:
        try:
            update_input = input("Enter Student ID (or 'back' to cancel): ").strip()

            if update_input.lower() == "back":
                return

            student_id= int(update_input)

            if student_id > 0:
                break
            else:
                print("ID must be positive")

        except ValueError:
            print("\"Enter a valid number\"")


    for student in student_list:

        if student.get_id() == student_id:

            while True:
                choice = input("""
What do you want to update?
1. Name
2. Age
3. Grade
4. Course
5. Semester
6. Back

Enter your choice: 
""").strip()

                if choice == "1":
                    while True:
                        new_name= input("Enter New Name (or 'back' to cancel): ").strip().title()

                        if new_name.lower() == "back":
                            return

                        if new_name and all(character.isalpha() or character in " '-" for character in new_name) and any(character.isalpha() for character in new_name):
                            result= student.set_name(new_name)

                            if result:
                                print("\"Name UPDATED SUCCESSFULLY\"")
                                break

                        else: 
                            print("Invalid Name")


                elif choice == "2":

                    while True:
                        try:
                            age_input = input("Enter New Age (or 'back' to cancel): ").strip()

                            if age_input.lower() == "back":
                                return

                            new_age= int(age_input)
                            result = student.set_age(new_age)

                            if result:
                                print("\"Age UPDATED SUCCESSFULLY\"")
                                break

                        except ValueError:
                            print("Enter a valid number")

                elif choice == "3":
                    while True:
                        new_grade = input("Enter New Grade (A+, A, B+, B, C, D, F) or 'back' to cancel: ").upper().strip()

                        if new_grade == "BACK":
                            return

                        result = student.set_grade(new_grade)

                        if result:
                            print("\"Grade UPDATED SUCCESSFULLY\"")
                            break

                elif choice == "4":
                    while True:

                        new_course= select_course()

                        if new_course is None:
                            return

                        result = student.set_course(new_course)

                        if result:
                            print(f"Course UPDATED SUCCESSFULLY - {new_course}")
                            break

                elif choice == "5":
                    while True:
                        try:
                            semester_input= input("Enter New Semester(1-8) or 'back' to cancel: ").strip().lower()

                            if semester_input== "back":
                                return

                            new_semester= int(semester_input)
                            result = student.set_semester(new_semester)

                            if result:
                                print("\"Semester UPDATED SUCCESSFULLY\"")
                                break 

                        except ValueError:
                            print("Enter a valid number")

                elif choice == "6":
                    return

                else:
                    print("INVALID UPDATE CHOICE")
                    continue
                save_students()
                break # breaking while loop if choice is valid
            break #stopping for loop for unnecesarry search otherwise else will run  
    else:
        print("Student not found")



def delete_student():
    if not student_list:
        print("NO STUDENT AVAILABLE")
        return

    while True:
        try:
            student_id_input = input("Enter Student ID (or 'back' to cancel): ").strip().lower()

            if student_id_input== "back":
                return

            student_id= int(student_id_input)

            if student_id > 0:
                break
            else:
                print("ID must be positive")

        except ValueError:
            print("\"Enter a valid number\"")

    for student in student_list:

        if student.get_id() == student_id:
            while True:
                confirmation= input("Are you sure you want to delete this student? (y/n): ").lower().strip()

                if confirmation == "y":
                    student_list.remove(student)
                    save_students()
                    print("\"Student deleted successfully\"")
                    break
                elif confirmation == "n":
                    print("Deletion Cancelled")
                    break
                else:
                    print("Please enter y or n")
            break
    else:
        print("Student Not found!")


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


# In[ ]:




