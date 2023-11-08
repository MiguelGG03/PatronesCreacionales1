import sys
sys.path.append('../')
from pizzaBuilder import *
import validator
from config import TAMANOS , SALSAS , INGREDIENTES
from helpers import *

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
    pregunta = input("Buenas!\n"
                      "Que pizza vasa desear tomar?\n"
                      "1. Cuatro Quesos\n"
                      "2. Barbacoa\n"
                      "3. Margarita\n"
                      "4. Personalizada\n"
                      ">>>")
    if(pregunta == "1"):
        waiter.pizzaBuilder = CuatroQuesosPizzaBuilder()
        print("Que tamaño deseas:")
        printTamanos()
        tamano = input(">>> ")
        tamano = tamanoTranslator(tamano)
        print("Que masa deseas:")
        printMasas()
        masa = input(">>> ")

    elif(pregunta == "4"):
        waiter.pizzaBuilder = PersonalizadaPizzaBuilder()
        printIngredientes()
        print("Seleccione un total de tres ingredientes numéricamente."
              "\nPresione enter si desea no añadir mas ingredientes")
