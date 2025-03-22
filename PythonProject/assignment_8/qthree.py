class Animal():
    def __init__(self,name,species):
        self.name = name
        self.species = species
class Cat(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)
    def meow(self):
        print(self.species,"<--species", self.name,"<--name Meow");
class Dog(Animal):
    def __init__(self,name, species):
        super().__init__(name, species)
    def bark(self):
        print(self.species, "<--species", self.name, "<--name Bark");

obj = Cat("one","cat")
obj.meow()

obj1 = Dog("two","dog")
obj1.bark()