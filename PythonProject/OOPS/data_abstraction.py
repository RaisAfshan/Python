from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod

    def mileage(self):
        pass

class Tesla(Car):

    def mileage(self):
        print("the mileage is 30kmph")

class Suzuki(Car):
    def mileage(self):
        print("the mileage is 40kmph")

o = Tesla()
o.mileage()

o1=Suzuki()
o1.mileage()



