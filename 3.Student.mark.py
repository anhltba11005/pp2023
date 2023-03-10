import curses; curses.setupterm()               #; curses.setupterm()  this code to run code on window, dont need on linux
import math
import numpy as np


class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
    
    def __str__(self):
        return f"{self.id}_{self.name}_{self.DoB}"


class Course:
    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits
        self.marks = {}

    def input_mark(self, std, mark):
        self.marks[std] = mark

    def show_marks(self):
        for std, mark in self.marks.items():
            print(std, mark)

    def __str__(self):
        return f"{self.id}_{self.name}"


class School:
    def __init__(self):
        self.stds = []
        self.courses = []

    def input_num_std(self):
        self.num_std = int(input("Input number of students: "))

    def input_infor_std(self):
        for i in range(self.num_std):
            id = input(f"Input id of student No.{i+1}: ")
            name = input(f"Input name of student No.{i+1}: ")
            DoB = input(f"Input date of birth of student No.{i+1} (DD/MM/YYYY): ")
            std = Student(id, name, DoB)
            self.stds.append(std)

    def input_num_course(self):
        self.num_course = int(input("Input number of courses: "))

    def input_infor_course(self):
        for i in range(self.num_course):
            id = input(f"Input id of course No.{i+1}: ")
            name = input(f"Input name of course No.{i+1}: ")
            credits = float(input(f"Input credits of course No.{i+1}: "))
            course = Course(id, name, credits)
            self.courses.append(course)

    def input_mark(self):
        for course in self.courses:
            print(f"\nInput marks for course: {course.name} (id: {course.id})")
            for std in self.stds:
                mark = input(f"Input mark for student {std.name} (id: {std.id}): ")
                mark = math.floor(float(mark) * 10) / 10.0
                course.input_mark(std, mark)

    def list_stds(self):
        print("List of students:")
        for std in self.stds:
            print(std.id, std.name, std.DoB)

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(course.id, course.name, course.credits)

    def show_student_marks(self):
        for course in self.courses:
            print(f"\nShowing marks for course: {course.name} (id: {course.id})")
            for std, mark in course.marks.items():
                print(std.name, mark)

    def calculate_GPA(self, std):
        total_mark = 0
        total_credit = 0
        for course in self.courses:
            if std in course.marks:
                mark = course.marks[std]
                credit = course.credits
                total_mark += mark * credit
                total_credit += credit
        if total_credit == 0:
            return 0
        else:
            return total_mark / total_credit
    def show_GPA(self):
        print("GPA of students:")
        temp_list = []
        for std in self.stds:
            gpa = self.calculate_GPA(std)
            temp_list.append((std.name, gpa))
        sorted_list = sorted(temp_list, key=lambda x: x[1], reverse=True)
        for std, gpa in sorted_list:
            print(f"{std}: {gpa}")

 
def run():
    my_school = School()
    
    while True:
        print('''
1. Input number of students want to add to the students list
2. Input student information want to add to the students list
3. Input number of courses want to add to the courses list
4. Input course information want to add to the courses list
5. Input marks
6. List students
7. List courses
8. Show student marks
9. Show GPA of students
10. Exit
        ''')
        choice = input("Enter your choice (1-10): ")
        if choice == "1":
            my_school.input_num_std()
        elif choice == "2":
            my_school.input_infor_std()
        elif choice == "3":
            my_school.input_num_course()
        elif choice == "4":
            my_school.input_infor_course()
        elif choice == "5":
            my_school.input_mark()
        elif choice == "6":
            my_school.list_stds()
        elif choice == "7":
            my_school.list_courses()
        elif choice == "8":
            my_school.show_student_marks()
        elif choice == "9":
            my_school.show_GPA()
        elif choice == "10":
            print("Exit program")
            break
        else:
            print("Invalid choice. Please enter a number between 1-10.")

run()
