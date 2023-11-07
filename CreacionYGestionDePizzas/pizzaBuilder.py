import sys
sys.path.append('../')
from pizza import Pizza

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def setDough(self, dough):
        self.pizza.dough = dough

    def setSauce(self, sauce):
        self.pizza.sauce = sauce

    def setTopping(self, topping):
        self.pizza.topping = topping

    def getPizza(self):
        return self.pizza