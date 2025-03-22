class Vehicle():
    def max_speed(self):
        print("speed of the car is 200")

class Car(Vehicle):
    def max_speed(self):
        print("speed limit of the car is 80")

obj = Car()
obj.max_speed()