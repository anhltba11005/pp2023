from domains.student import Student
from domains.course import Course
import math

# Input informations of students
def input_num_std(self):
    self.num_std = int(input("Input number of students: "))

def input_infor_std(self):
    for i in range(self.num_std):
        id = input(f"Input id of student No.{i+1}: ")
        name = input(f"Input name of student No.{i+1}: ")
        DoB = input(f"Input date of birth of student No.{i+1} (DD/MM/YYYY): ")
        std = Student(id, name, DoB)
        self.stds.append(std)
# Input informations of courses
def input_num_course(self):
    self.num_course = int(input("Input number of courses: "))

def input_infor_course(self):
    for i in range(self.num_course):
        id = input(f"Input id of course No.{i+1}: ")
        name = input(f"Input name of course No.{i+1}: ")
        credits = float(input(f"Input credits of course No.{i+1}: "))
        course = Course(id, name, credits)
        self.courses.append(course)

#Input marks
def input_mark(self):
    for course in self.courses:
        print(f"\nInput marks for course: {course.name} (id: {course.id})")
        for std in self.stds:
            mark = input(f"Input mark for student {std.name} (id: {std.id}): ")
            mark = math.floor(float(mark)* 10)/ 10.0
            course.input_mark(std, mark)