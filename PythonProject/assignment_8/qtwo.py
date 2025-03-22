from abc import ABC,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Sqaure(Shape):
    def calculate_area(self,a):
        result = a*a
        print(result)
class Circle(Shape):
    def calculate_area(self,r):
        result = 3.14*(r**2)
        print(result)

obj = Sqaure()
obj.calculate_area(2)

obj1 = Circle()
obj1.calculate_area(4.0)