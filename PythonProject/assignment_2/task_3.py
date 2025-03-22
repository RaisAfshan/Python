class Vehicle():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        c = self.x + self.y
        print("add-->",c)

    def multi(self):
        c = self.x * self.y
        print("multiply-->",c)

obj1 = Vehicle(3,4)
obj2 = Vehicle(5,7)
obj3 = Vehicle(4,6)
obj4 = Vehicle(8,3)

obj1.add()
obj1.multi()
obj2.add()
obj2.multi()
obj3.add()
obj3.multi()
obj4.add()
obj4.multi()

