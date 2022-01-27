from datetime import date
from time import perf_counter

class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def _print(self):
        s = f'Name - {self.name}\nAge - {self.age}'
        return s

class Enrollee(Person):
    def __init__(self, name, age, facult):
        super().__init__(name, age)
        self.facult = facult

    def _print(self):
        return super()._print() + f'\nFaculty - {self.facult}'

class Student(Person):

    def __init__(self, name, age, faculty, course):
        super().__init__(name, age)
        self.faculty = faculty
        self.course = course
    
    def _print(self):
        return super()._print() + f'\nFaculty - {self.facult}\Course - {self.course}'

class Teacher(Person):

    def __init__(self, name, age, faculty, position, exp):
        super().__init__(name, age)
        self.faculty = faculty
        self.position = position
        self.exp = exp

    def _print(self):
        return super()._print() + f'\nFaculty - {self.facult}\Position - {self.position}\Experience - {self.exp}'

# Bob = Enrollee('Bob', '22', 'Math')

# print(Bob._print())



# self.age = date.today().year - b_day.year