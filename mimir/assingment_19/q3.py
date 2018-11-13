class Student:
    def __init__(self, student_id, student_grades):
        self.student_id = student_id
        self.student_grades = [float(i) for i in student_grades]
    def __gt__(self, other):
        average1 = self.ave()
        average2 = other.ave()
        return average1 > average2   
    def ave(self):
        ave = sum(self.student_grades) / len(self.student_grades)
        return ave
    def __str__(self):
        return "Student ID: {}\nGrades: {}".format(self.student_id, self.student_grades)