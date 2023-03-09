#Create class Std (mean Student) 
class Std:
    def __init__(self, id, name, DoB):
        self.id= id
        self.name= name
        self.DoB= DoB
    
    def __str__(self):
        return f"{self.id}_{self.name}_{self.DoB}"
#Create class Course    
class Course:
    def __init__(self, id, name):
        self.id= id
        self.name= name
        self.marks= {}

    def input_mark(self, std, mark):
        self.marks[std]= mark

    def show_marks(self):
        for std, mark in self.marks.items():
            print(std, mark)
    
    def __str__(self):
        return f"{self.id}_{self.name}"
    
#Create class School that def func to input in4 stds, course, mark and show them
class School:
    def __init__(self):
        self.stds = []
        self.courses = []

    # Input informations of students
    def input_num_std(self):
        self.num_std = int(input("Input number of student: "))

    def input_infor_std(self):
        for i in range(self.num_std):
            id = input(f"Input id of student No.{i+1}: ")
            name = input(f"Input name of student No.{i+1}: ")
            DoB = input(f"Input day of birth of student No.{i+1}: ")
            std = Std(id, name, DoB)
            self.stds.append(std)

    # Input information of courses
    def input_num_course(self):
        self.num_course = int(input("Input number of course: "))

    def input_infor_course(self):
        for i in range(self.num_course):
            id = input(f"Input id of course No.{i+1}: ")
            name = input(f"Input id of name No.{i+1}: ")
            course = Course(id, name)
            self.courses.append(course)

    #Input marks
    def input_mark(self):
        for course in self.courses:
            print(f"\nInput marks for course: {course.name} (id: {course.id})")
            for std in self.stds:
                mark = input(f"Input mark for student {std.name} (id: {std.id}): ")
                course.input_mark(std, mark)
    #Print students and courses list, show marks
    def list_stds(self):
        for std in self.stds:
            print(std.id, std.name, std.DoB)

    def list_courses(self):
        for course in self.courses:
            print(course.id, course.name)

    def show_student_marks(self):
        for course in self.courses:
            print(f"\nShowing marks for course: {course.name} (id: {course.id})")
            course.show_marks()

#Function to run
def run():
    my_school= School()
    
    #Create a list options
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
9. Exit
        ''')
        choice = input("Enter your choice (1-9): ")
        if choice== "1":
            my_school.input_num_std()
        elif choice== "2":
            my_school.input_infor_std()
        elif choice== "3":
            my_school.input_num_course()
        elif choice== "4":
            my_school.input_infor_course()
        elif choice== "5":
            my_school.input_mark()
        elif choice== "6":
            my_school.list_stds()
        elif choice== "7":
            my_school.list_courses()
        elif choice== "8":
            my_school.show_student_marks()
        elif choice== "9":
            print("Exit program")
            break
        else:
            print("Invalid choice. Please enter a number between 1-9.")

run()
