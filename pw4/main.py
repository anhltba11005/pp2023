from domains.school import School
import curses; curses.setupterm()               #; curses.setupterm()  this code to run code on window, dont need on linux
import numpy as np
def run():
    my_school = School()
    
    
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
