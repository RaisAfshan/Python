class Transport():
    def mode_of_transport(self):
        print("mode of transport")

class Airplane(Transport):
    def mode_of_transport(self):
        print("Air")

class Boat(Airplane):
    def mode_of_transport(self):
        print("Water")
        super().mode_of_transport()

obj = Boat()
obj.mode_of_transport()