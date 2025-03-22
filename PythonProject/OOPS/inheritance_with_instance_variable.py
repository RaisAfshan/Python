class College():
    collegename = "tkmce"
    def __init__(self,name):
        self.name = name

class Student(College):
    def __init__(self,name,course,mark):
        self.course = course
        self.mark = mark
        super().__init__(name)
    def display(self):
        print(self.course, self.name , self.mark,College.collegename)

obj = Student("john","python",88)
obj.display()
