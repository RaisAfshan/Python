class Student():
    name = "John"

    def __init__(self,name1):
        self.name1 = name1
    @classmethod
    def demo(cls):
        print("classmethod-->",cls.name)

    def demo1(self):
        print("inctance method",self.name1)

    @staticmethod
    def demo2(name2):
        print("staticmethod --->",name2)

obj = Student("wick")
obj.demo()
obj.demo1()
obj.demo2("terry")