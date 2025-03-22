class Example():
    def __init__(self):
        self.__a = "private data"

    def get_data(self): #getter method
        print(self.__a)

    def det_Data(self): #setter method
        self.__a = "data 2"

obj = Example()
obj.get_data()
obj.det_Data()
obj.get_data()