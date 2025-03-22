class F:
    def __init__(self,x,y):
        self.x = x
        self.y = y
class B(F):
    def __init__(self,x,y):
        F.__init__(self,x,y)

    def display(self):
        print(self.x,self.y);

class A(B):
    def __init__(self,x,y,z):
        self.z = z
        super().__init__(x,y)

    def display(self):
        print(self.x,self.y,self.z)

class E(F):
    def __init__(self,x,y):
        F.__init__(self,x,y)

    def add(self):
        c = self.x + self.y
        print("sum = ",c)

obj = A(1,2,3)
obj.display()

obj2 = E(5,7)
obj2.add()