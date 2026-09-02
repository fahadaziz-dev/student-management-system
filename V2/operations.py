from data import student_list
from student import Student
from constants import valid_grades, programs
from file_manager import save_students

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
    
    
        while True:
    
            try:
                id_input = input("Enter ID (or 'back' to cancel): ").strip()
    
                if id_input.lower() == "back":
                    return
    
                st_id= int(id_input)

                if st_id > 0:
                    break
                else:
                    print("ID must be positive")
                    continue
                    
            except ValueError:   
                print("\"Enter a valid number\"")

        duplicate_exists = False

        for student in student_list:
            if student.get_semester() == semester and student.get_id() == st_id:
                duplicate_exists = True
                break

        if duplicate_exists:
            print("\nA student with this ID already exists in this semester.")
            print("Please use a different Student ID or select a different semester.")
            continue

        break
        
    while True:

        grade = input("Enter Grade (A+, A, B+, B, C, D, F) or 'back' to cancel: ").upper().strip()

        if grade == "BACK":
            return
            
        if grade in valid_grades:
            break
        else:
            print("INVALID GRADE")

    selected_program_rt= select_program()
    
    if selected_program_rt is None:
        return

    print(f"Program Selected Successfully - {selected_program_rt}")
            
    student = Student(name, age, semester, st_id, grade, selected_program_rt)
    student_list.append(student)
    save_students()

    print("\"Student Added Successfully\"")


def display_students():

    if not student_list:
        print("NO STUDENT FOUND!")
        return

    print(f"{'ID':<6}{'Name':<15}{'Age':<6}{'Program':<35}{'Sem':<6}{'Grade':<6}")

    for student in student_list:
        print(f"{student.get_id():<6}{student.get_name():<15}{student.get_age():<6}{student.get_program():<35}{student.get_semester():<6}{student.get_grade():<6}")


def display_student(student):

    print(f"""
---STUDENT DETAILS---
Name: {student.get_name()}
Age: {student.get_age()}
ID: {student.get_id()}
Program: {student.get_program()}
Semester: {student.get_semester()}
Grade: {student.get_grade()}
---------------------""")


def search_student():    
    if not student_list:
        print("NO STUDENT AVAILABLE")
        return
    
    while True:
        try:
            id_input = input("Enter Student ID (or 'back' to cancel): ").strip()

            if id_input.lower() == "back":
                return

            student_id= int(id_input)
            
            if student_id > 0:
                break
            else:
                print("ID must be positive")

        except ValueError:
            print("\"Enter a valid number\"")

    while True:
        try:
            semester_input = input("Enter Semester(1-8) or 'back' to cancel: ").strip()

            if semester_input.lower() == "back":
                return

            student_semester= int(semester_input)
            
            if 1 <= student_semester <= 8:
                break
            else:
                print("Semester must be between 1 and 8")

        except ValueError:
            print("\"Enter a valid number\"")

    
    for student in student_list:

        if student.get_id() == student_id and student.get_semester() == student_semester:
            display_student(student)
            break

    else:
        print("Student NOT FOUND!")


def select_program():
    while True:
        print("\n===== AVAILABLE PROGRAMS =====")
        for i, program in enumerate(programs, start=1):
            print(f" {i}. {program}")

        try:
            program_input= input("Enter Program Number (or 'back' to cancel): ").strip()

            if program_input.lower() == "back":
                return None

            program_number = int(program_input)
            
            if 1 <= program_number <= len(programs):
                selected_program= programs[program_number-1]
                return selected_program
            else:
                print("Invalid Program Selection")
                
        except ValueError:
            print("Invalid Number")
    
def update_student():
    if not student_list:
        print("NO STUDENT AVAILABLE")
        return

    
    while True:
        try:
            id_input = input("Enter Student ID (or 'back' to cancel): ").strip()

            if id_input.lower() == "back":
                return

            student_id= int(id_input)
            
            if student_id > 0:
                break
            else:
                print("ID must be positive")

        except ValueError:
            print("\"Enter a valid number\"")

    while True:
        try:
            semester_input = input("Enter Semester(1-8) or 'back' to cancel: ").strip()

            if semester_input.lower() == "back":
                return

            student_semester= int(semester_input)
            
            if 1 <= student_semester <= 8:
                break
            else:
                print("Semester must be between 1 and 8")

        except ValueError:
            print("\"Enter a valid number\"")

    
    for student in student_list:
        if student.get_id() == student_id and student.get_semester() == student_semester:

            while True:
                choice = input("""
What do you want to update?
1. Name
2. Age
3. Grade
4. Program
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
                        
                        new_program= select_program()

                        if new_program is None:
                            return
                            
                        result = student.set_program(new_program)
    
                        if result:
                            print(f"Program UPDATED SUCCESSFULLY - {new_program}")
                            break
    
                elif choice == "5":
                    while True:
                        try:
                            semester_input= input("Enter New Semester(1-8) or 'back' to cancel: ").strip()

                            if semester_input.lower()== "back":
                                return

                            new_semester= int(semester_input)

                            if 1 <= new_semester <= 8:
                                pass
                            else:
                                print("Semester must be between 1 and 8")
                                continue
                                
                            duplicate_exists= False

                            if new_semester == student.get_semester():
                                print("Student is already in this semester")
                                continue
                            
                            for other_student in student_list:
                                if other_student.get_id() == student.get_id() and other_student.get_semester() == new_semester:
                                    duplicate_exists= True
                                    break

                            if duplicate_exists:
                                print("This Student ID already exists in the selected semester")
                                continue
                            else:
                                result = student.set_semester(new_semester)
                                
                            if result:
                                print("\"Semester UPDATED SUCCESSFULLY\"")
                                break 
                            else:
                                print("Could not update semester")
    
                        except ValueError:
                            print("Enter a valid number")
                            
                elif choice == "6":
                    return
            
                else:
                    print("INVALID UPDATE CHOICE")
                    continue
                save_students()
                break # breaking while loop if choice is valid
            break # stopping for loop for unnecesarry search otherwise else will run  
    else:
        print("Student not found")

def delete_student():
    if not student_list:
        print("NO STUDENT AVAILABLE")
        return
    
    while True:
        try:
            student_id_input = input("Enter Student ID (or 'back' to cancel): ").strip()
            
            if student_id_input.lower() == "back":
                return

            student_id= int(student_id_input)
                
            if student_id > 0:
                break
            else:
                print("ID must be positive")

        except ValueError:
            print("\"Enter a valid number\"")

    while True:
        try:
            semester_input = input("Enter Semester(1-8) or 'back' to cancel: ").strip()

            if semester_input.lower() == "back":
                return

            student_semester= int(semester_input)
            
            if 1 <= student_semester <= 8:
                break
            else:
                print("Semester must be between 1 and 8")

        except ValueError:
            print("\"Enter a valid number\"")

    for student in student_list:

        if student.get_id() == student_id and student.get_semester() == student_semester:
            display_student(student)
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
