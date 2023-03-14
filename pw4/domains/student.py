#Create class Std (mean Student) 
class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
    
    def __str__(self):
        return f"{self.id}_{self.name}_{self.DoB}"