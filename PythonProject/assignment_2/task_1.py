class Vehicles():
    def __init__(self,speed,mileage):
        self.speed = speed
        self.mileage = mileage

    def display(self):
        print(self.speed,self.mileage)

obj = Vehicles(170,40)
obj.display()
        