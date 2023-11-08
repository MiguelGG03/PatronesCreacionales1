import sys
sys.path.append('../')
from pizzaBuilder import PizzaBuilder

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
