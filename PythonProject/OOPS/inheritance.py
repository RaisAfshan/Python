class College():
    def __init__(self):
        print("constructor one")

    def name(self):
        print("TKMCE")

class Student(College):

    def __init__(self):
        print("constructor two") 
        College.__init__(self) #to call constructor of parent class

    def studentname(self):
        print("john")

obj = Student()
obj.name()
obj.studentname()