
class Course:
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit

    def get_credit(self):
        return self.credit


class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def total_credit(self):
        sum = 0
        for course in self.courses:
            sum += course.get_credit()
        return sum 


a = Student("John Doe", "IT")
a.add_course(Course('Algebra', 3))
a.add_course(Course('Python', 4))
a.add_course(Course('MIS', 4))

print(a.total_credit())