import sys
sys.path.append('../')
from pizzaBuilder import *

class Waiter:
    def __init__(self):
        self.pizzaBuilder = None
    
    def setPizzaBuilder(self,pizzaBuilder:PizzaBuilder):
        self.pizzaBuilder = pizzaBuilder
    
    def getPizza(self):
        return self.pizzaBuilder.getPizza()
    
    def buildPizza(self,*args,**kwargs):
        self.pizzaBuilder.build(*args,**kwargs)