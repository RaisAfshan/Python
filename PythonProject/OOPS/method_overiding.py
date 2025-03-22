class Car():
    def speed(self):
        print("speed of the car 300")

    def color(self):
        print("color of the red")

class Car1(Car):
    def speed(self):
        print("speed of the car 400")
        super().speed()

    def color(self):
        print("color of the green")
        super().color()


obj = Car1()
obj.speed()
obj.speed()