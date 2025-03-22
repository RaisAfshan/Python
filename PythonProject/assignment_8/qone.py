class Vehicles():
    make = "Car"
    model = "A8"
    @classmethod
    def print_info(cls):
        print(cls.make,cls.model)
class Car(Vehicles):
    num_doors = "4"
    @classmethod
    def print_info(cls):
        print(cls.num_doors,cls.make,cls.model)
class Motorcycle(Vehicles):
    engine_size = "4kg"
    def print_info(cls):
        print(cls.engine_size,cls.make,cls.model)

obj = Motorcycle()
obj.print_info()
obj2 = Car()
obj.print_info()
