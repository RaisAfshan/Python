from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        a=10
        print("the dog barks",a)

class Cat(Animal):
    def sound(self):
        print("Meow")

obj = Cat()
obj.sound()
obj1 = Dog()
obj1.sound()


