class Circle():
    def get_color(self,c):
        print("color of the circle is ",c)

class Circle2(Circle):
    def get_color(self,r):
        print("radius of the the circle ",r)
        super().get_color("red")

obj = Circle2()
obj.get_color(3)

