class Sum():
    def add(self,a,b,c):
        result = a+b+c
        print(result)

    def add(self,a,b,c=0):
        result = a+b
        print(result)

obj1 = Sum()
obj1.add(1,2,3)
obj1.add(1,5)
s={1,2,3}
s1={3,5,6}


square= lambda x:x**2
a=[]
for i in range(5):
    a.append(square(i))
print(a)