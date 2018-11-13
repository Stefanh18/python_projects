# Dæmatímaverk_7_Haukura18_Halldorv18_Stefanh18_Vytautas18.pdf

class Person:
    def __init__(self,name="",userName="",SSN=0):
        self.__name = str(name)
        self.__username = str(userName)
        self.__ssn = int(SSN)

    def get_name(self):
        return self.__name

    def get_username(self):
        return self.__username

    def get_ssn(self):
        return self.__ssn

class Student(Person):
    def __init__(self,department="",name="",userName="",SSN=0):
        self.__department = str(department)
        Person.__init__(self,name,userName,SSN)

    def get_department(self):
        return self.__department

class Professor(Person):
    def __init__(self,position="",name="",userName="",SSN=0):
        self.__position = str(position)
        Person.__init__(self,name,userName,SSN)

    def get_position(self):
        return self.__position    

class course():
    def __init__(self,students,professor,name=""):
        self.__name = str(name)
        self.__students = []
        self.__professor = professor

    def get_name(self):
        return self.__name

    def get_student(self):
        return self.__students

    def get_professor(self):
        return self.__professor