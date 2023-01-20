from .Bachelor import Bachelor, Student
from .Aspirant import Aspirant


def print_students(*students: Student):
    for student in students:
        print(student)


def test():
    student_bachelor = Bachelor('Nikolay', '1011', 4)
    student_aspirant = Aspirant('Misha', '12312', 3.4)
    print_students(student_bachelor, student_aspirant)
    student_aspirant.update_average_mark(5)
    student_bachelor.update_average_mark(2)
    print_students(student_bachelor, student_aspirant)


if __name__ == '__main__':
    test()
