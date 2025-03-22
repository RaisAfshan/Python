class BankAccount():
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,dep):
        self.__balance = self.__balance+dep

    def withdraw(self,w):
        self.__balance = self.__balance - w

    def get_data(self):
        print("Balance -->",self.__balance)


obj = BankAccount(2000)
obj.get_data()
obj.withdraw(50)
obj.get_data()
obj.deposit(1000)
obj.get_data()

