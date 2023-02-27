#Function to input number
def input_num(object):
    return int(input(f"Please enter the number of {object}: "))

#Input informations for objects
def input_infors(obj_type, infors):
    obj= {}
    for infor in infors:
        obj[infor]= input(f"Enter the {obj_type}'s of {infor}: ")
    return obj

#Input marks of courses
def input_mark(std, course_id):
    if "marks" not in std:
        std["marks"]= {}
    std["marks"][course_id]= input(f"Enter the student's mark of course {course_id}: ")

#Display list of objects
def display(list):
    for i, obj in enumerate(list):
        print(f"{i+1}. {obj}")

#Display list of students
def display_std(stds):                       
    if len(stds)<=0:
        print("There's no student here!")
        return
    print("There is the student list: ")
    for i, std in enumerate(stds):
        print(f"{i+1}. {std['id']}_ {std['name']}_ {std['DoB']}")
        if "marks" in std:
            for course_id, course_name, mark, in std["marks"].obj():
                print(f"Marks of {course_id}_ {course_name}: {mark}", end="\n")
            print()

#Display list of courses
def display_courses(courses):
    if len(courses)<=0:
        print("There's no course here")
        return
    print("there are courses list: ")
    for i, course in enumerate(courses):
        print(f"{i+1}. {course['id']}_ {course['name']}")

#Input integer to select an option
def select_option(option_number, input_select= "Please choose any option: "):
    slt= input(input_select)
    if not slt.isnumeric():
        return -1
    slt= int(slt)
    if slt not in option_number:
        return -1
    return slt

#Function to pause programme
def pause():
    input("Enter to contine...")

#Main function
def main():
    stds= []
    courses= []
    num_std= 0
    num_courses= 0

    #create list options
    while(True):
        print('''
        Please choose options:
        1. Input number of students
        2. Input number of courses
        3. Input informations of students(id, name, DoB)
        4. Input informations of courses(id, name)
        5. Input mark
        6. Print students list
        7. Print courses list
        8. Exit progamme
        ''')
        slt= select_option(range(1,8))
        if slt== 1:
            num_std= input_num("student")
            if num_std== 1:
                print(f"There are 1 student in students list")
            else:
                print(f"There are {num_std} students in students list")
        elif slt==2:
            num_courses= input_num("course")
            if num_courses== 1:
                print(f"There are 1 course in courses list")
            else:
                print(f"There are {num_courses} courses in courses list")
        elif slt==3:
            if num_std<=0:
                print("Plese input number of students first")
                pause()
                continue
            else:
                print("There are students list: ")
                stds= []
                for i in range(num_std):
                    print(f"Student no.{i+1}")
                    stds.append(input_infors("students",("id", "name", "DoB")))
                    display_std(stds)
        elif slt==4:
            if num_courses<=0:
                print("Please input number of courses first")
                pause()
                continue
            else:
                print("There are course list: ")
                courses= []
                for i in range(num_courses):
                    print(f"Course no.{i+1}")
                    courses.append(input_infors("course",("id", "name")))
                display_courses(courses)
        elif slt==5:
            display_courses(courses)
            if len(courses)> 0:
                sl_course= select_option(range(1, num_courses+ 1), "Please select a course: ")
                if sl_course< 0:
                    print("There's not option in the list")
                else:
                    for i in range(num_std):
                        print(f"Student no.{i+1}_{stds[i]['name']}: ")
                        input_mark(stds[i], courses[sl_course]["id"])
        elif slt==6:
            display_std(stds)
        elif slt==7:
            display_courses(courses)
        elif slt==8:
            break
        else:
            print("Try again")
        pause()
#Run
if __name__ =="__main__":
	main()



    
