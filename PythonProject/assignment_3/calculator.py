class Calculator():

    def add(self,x,y):
        result = x+y
        print("add -->",result)

    def sub(self,x,y):
        result = x-y
        print("substract -->",result)

    def multi(self,x,y):
        result = x*y
        print("multiple -->",result)

    def division(self,x,y):
        result = x/y
        print("division -->",result)

obj = Calculator()
obj.add(3,4)
obj.sub(4,5)
obj.multi(6,8)
obj.division(4,9)