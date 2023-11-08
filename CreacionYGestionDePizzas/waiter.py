import sys
sys.path.append('../')
from pizzaBuilder import *
from config import TAMANOS , SALSAS , INGREDIENTES
from helpers import printIngredientes

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
    pregunta1 = input("Buenas!\n"
                      "Que pizza vasa desear tomar?\n"
                      "1. Cuatro Quesos\n"
                      "2. Barbacoa\n"
                      "3. Margarita\n"
                      "4. Personalizada\n"
                      ">>>")
    if(pregunta1 == "1"):
        waiter.pizzaBuilder = CuatroQuesosPizzaBuilder()





    elif(pregunta1 == "4"):
        print("Seleccione un total de tres ingredientes numéricamente."
              "\nPresione enter si desea no añadir mas ingredientes")
