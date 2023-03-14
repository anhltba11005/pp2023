from inputt import input_num_std, input_infor_std, input_num_course, input_infor_course, input_mark
from output import list_stds, list_courses, show_student_marks, show_GPA

class School:
    def __init__(self):
        self.stds = []
        self.courses = []
    #Call input func    
    def input_num_std(self):
        input_num_std(self)
    def input_infor_std(self):
        input_infor_std(self)
    def input_num_course(self):
        input_num_course(self)
    def input_infor_course(self):
        input_infor_course(self)
    def input_mark(self):
        input_mark(self)

    #Call output func
    def list_stds(self):
        list_stds(self)
    def list_courses(self):
        list_courses(self)
    def show_student_marks(self):
        show_student_marks(self)
    #Func to cal GPA
    def calculate_GPA(self, std):
        total_mark= 0
        total_credit= 0
        for course in self.courses:
            if std in course.marks:
                mark= course.marks[std]
                credit= course.credits
                total_mark+= mark* credit
                total_credit+= credit
        if total_credit== 0:
            return 0
        else:
            return total_mark/ total_credit

    #Fuction to show GPA
    def show_GPA(self):
        show_GPA(self)

    