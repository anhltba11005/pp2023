#Create class Course, add attribute credits
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
        return f"{self.id}_{self.name}_{self.credits}"