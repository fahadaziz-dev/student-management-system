from data import student_list
import os
from student import Student
from constants import valid_grades, programs

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "students.txt")

def save_students():
    try:
        with open(FILE_PATH, "w") as file:
            for student in student_list:
                file.write(f"{student.get_name()},{student.get_age()},{student.get_semester()},{student.get_id()},{student.get_grade()},{student.get_program()}\n")
    
        print("Data Saved Successfully")

    except OSError:
        print("Error: Could not save student data.")
        
def load_students():
    skipped_records= 0
    
    try:
        with open(FILE_PATH, "r") as file:
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

                    semester= int(data[2])
                    if not (1 <= semester <= 8):
                        skipped_records += 1
                        continue

                        
                    student_id= int(data[3])
                    if student_id <= 0:
                        skipped_records += 1
                        continue

                    st_exists= False
                    for student in student_list:
                        if student.get_id() == student_id and student.get_semester() == semester:
                            st_exists= True
                            break

                    if st_exists:
                        skipped_records += 1
                        print(f"Warning: Duplicate student ID {student_id} found within same semester {semester}. Record skipped.")
                        continue
                          
                    grade = data[4]
                    if grade not in valid_grades:
                        skipped_records += 1
                        continue

                    program = data[5]
                    if program not in programs:
                        skipped_records += 1
                        continue
                    
    
                    student= Student(name, age, semester, student_id, grade, program)
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
        
            with open(FILE_PATH, "w") as file:
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

    if not os.path.exists(FILE_PATH):
        print("\"File does not exist\"")
        return

    while True:
        print("Note: This will delete the saved file.")
        print("Current student data will remain available until the program is closed.")
        
        choice= input("Are you sure you want to delete the student file? (y/n): ").lower().strip()
        if choice == "y":
            os.remove(FILE_PATH)
            print("Student file deleted successfully.")
            print("Current session data is still available until the program exits.")
            break
     
        elif choice == "n":
            print("File deletion cancelled!")
            break

        else:
            print("Please enter 'y/n'")
            
# viewing file function
def view_file():
    try:
        with open(FILE_PATH, "r") as file:
            data= file.read()
    
            if data:
                print(data)
            else:
                print("No Data Found")

    except FileNotFoundError:
        print("File does not exist")
