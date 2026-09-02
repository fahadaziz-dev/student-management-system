from constants import valid_grades

class Student:
     
    def __init__(self, name, age, semester, student_id, grade, program):
        self.__name = name
        self.__age = age
        self.__student_id = student_id
        self.__program = program
        self.__semester = semester
        self.__grade = grade

    # getters
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_id(self):
        return self.__student_id

    def get_program(self):
        return self.__program

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

    def set_program(self, program):
        if program.strip():
            self.__program = program
            return True
        else:
            print("Program cannot be empty")
            return False

    def set_semester(self, semester):
        if 1 <= semester <= 8:
            self.__semester = semester
            return True
        else:
            print("Semester must be between 1 and 8")
            return False
# class structure ends
