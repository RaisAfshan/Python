class Machine():
    def spec(self):
        print("hello world")

class Computer(Machine):
    def spec(self):
        print("14inch monitor");
        print("i5 14th gen")
        print("rtx 2050")

class Laptop(Computer):
    def spec(self):
        print("14inch monitor 1440p res")
        print("i5 14th gen")
        print("rtx 4060")
        print("rgb keyboard backlight")

obj = Laptop()
obj.spec()