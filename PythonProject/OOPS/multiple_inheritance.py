class College():
    def __init__(self,name):
        self.name = name

class Course():
    def __init__(self,course):
        self.course = course

class Student(College,Course):
    def __init__(self,sname,cousre,name):
        self.sname = sname
        Course.__init__(self,cousre)
        College.__init__(self,name)

    def display(self):
        print("College name -->",self.name,"course-->", self.course , "student name -->",self.sname)

obj = Student("john","MCA","TKMCE")
obj.display()