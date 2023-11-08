import sys
sys.path.append('../')
from pizzaBuilder import *

class Waiter:
    def __init__(self):
        self._pizzaBuilder = None
    
    @property
    def pizzaBuider(self):
        return _pizzaBuilder

    @pizzaBuilder.setter
    def pizzaBuilder(self,pizzaBuilder):
        if(pizzaBuilder)
    
    def getPizza(self):
        return self.pizzaBuilder.getPizza()
    
    def buildPizza(self,*args,**kwargs):
        self.pizzaBuilder.build(*args,**kwargs)