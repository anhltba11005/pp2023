#Print students and courses list, show marks
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


#Fuction to show GPA
def show_GPA(self):
    print("GPA of students: ")
    temp_list= []
    for std in self.stds:
        gpa= self.calculate_GPA(std)
        temp_list.append((std.name, gpa))
    sorted_list= sorted(temp_list, key=lambda x: x[1], reverse=True)
    for std, gpa in sorted_list:
        print(f"{std}: {gpa}")