class Car():
    def __init__(self,name):
        self.name = name

class Color(Car):
    def __init__(self,color,name):
        self.color = color
        super().__init__(name)

class Door(Color):
    def __init__(self,door,name,color):
        self.door = door;
        super().__init__(name,color)

    def display(self):
        print("carname-->",self.name,"door-->",self.door,"color-->",self.color)

obj = Door("2-door", "ferrari spyder","red")
obj.display()