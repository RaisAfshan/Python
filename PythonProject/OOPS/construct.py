class Car():
    def __init__(self,name):
        self.name = name

    def demo(self):
        print("demo ",self.name)

obj = Car("hello")
obj.demo()
