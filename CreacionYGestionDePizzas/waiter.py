import sys
sys.path.append('../')
from pizzaBuilder import *

class Waiter:
    def __init__(self):
        self._pizzaBuilder = None
    
    @property
    def pizzaBuider(self):
        return self._pizzaBuilder

    @pizzaBuider.setter
    def pizzaBuilder(self,pizzaBuilder):
        if (isinstance(pizzaBuilder,PizzaBuilder)):
            self._pizzaBuilder = pizzaBuilder
    
    def getPizza(self):
        return self.pizzaBuilder.getPizza()
    
    def buildPizza(self,*args,**kwargs):
        self.pizzaBuilder.build(*args,**kwargs)

if __name__=='__main__':
    waiter = Waiter()
    waiter.pizzaBuilder = CuatroQuesosPizzaBuilder()
    waiter.buildPizza("mediana","fina")
    pizza = waiter.getPizza()
    print(pizza.to_csv())