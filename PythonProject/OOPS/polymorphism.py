class student1():
    def detail(self):
        print("student1 detail");

class student2():
    def detail(self):
        print("student2 detail ");

def demo(test):
    test.detail()
    test.detail()

obj = student1()
demo(obj)

obj1 = student2()
demo(obj1)