class Pizza():

    def smallPizza(self,rupees):
        print("small pizza price:" , rupees)
    def mediumPizza(self,rupees):
        print("medium pizza price:" , rupees)
    def largePizza(self,rupees):
        print("large pizza price:" , rupees)
class PizzaPaproni(Pizza):

    def smallPizza(self,rupees,paproni):
        print("price of small pizza with paproni = ",rupees+paproni)

    def mediumPizza(self,rupees,paproni):
        print("price of medium pizza with paproni = ",rupees+paproni)

    def largePizza(self,rupees,paproni):
        print("large pizza with papperroni = ",rupees+paproni)

class ExtraCheese(PizzaPaproni):
    def smallPizza(self,rupees,paproni,cheese):
        print("small pizza with papperoni with extra cheese : ",rupees+paproni+cheese)

    def mediumPizza(self,rupees,paproni,cheese):
        print("price of medium pizza with paproni = ",rupees+paproni+cheese)

    def largePizza(self,rupees,paproni,cheese):
        print("large pizza with papperroni = ",rupees+paproni+cheese)


obj = ExtraCheese()
obj.smallPizza(200,50,30)
obj.largePizza(300,40,20)

obj2 = ExtraCheese()
obj2.smallPizza(200,30,20)






















