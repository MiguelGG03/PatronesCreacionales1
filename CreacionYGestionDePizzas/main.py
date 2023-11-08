import sys
sys.path.append('../')
from waiter import Waiter
from pizzaBuilder import *
from helpers import *

def main():
    waiter = Waiter()
    pregunta = input("Buenas!\n"
                      "Que pizza vasa desear tomar?\n"
                      "1. Cuatro Quesos\n"
                      "2. Barbacoa\n"
                      "3. Margarita\n"
                      "4. Personalizada\n"
                      ">>> ")
    if(pregunta == "1"):
        waiter.pizzaBuilder = CuatroQuesosPizzaBuilder()
        print("Que tamaño deseas:")
        printTamanos()
        tamano = input(">>> ")
        tamano = tamanoTranslator(tamano)
        print("Que masa deseas:")
        printMasas()
        masa = input(">>> ")
        masa = masaTranslator(masa)
        waiter.buildPizza(tamano,masa)
        print(waiter.getPizza().to_csv())

    if(pregunta == "2"):
        waiter.pizzaBuilder = BarbacoaPizzaBuilder()
        print("Que tamaño deseas:")
        printTamanos()
        tamano = input(">>> ")
        tamano = tamanoTranslator(tamano)
        print("Que masa deseas:")
        printMasas()
        masa = input(">>> ")
        masa = masaTranslator(masa)
        waiter.buildPizza(tamano,masa)
        print(waiter.getPizza().to_csv())

    if(pregunta == "3"):
        waiter.pizzaBuilder = MargaritaPizzaBuilder()
        print("Que tamaño deseas:")
        printTamanos()
        tamano = input(">>> ")
        tamano = tamanoTranslator(tamano)
        print("Que masa deseas:")
        printMasas()
        masa = input(">>> ")
        masa = masaTranslator(masa)
        waiter.buildPizza(tamano,masa)
        print(waiter.getPizza().to_csv())

    elif(pregunta == "4"):
        waiter.pizzaBuilder = PersonalizadaPizzaBuilder()
        print("Ponle un nombre a tu pizza!\n"
              "Debe tener entre 4 y 16 caracteres")
        nombre = input(">>> ")
        print("Que tamaño deseas:")
        printTamanos()
        tamano = input(">>> ")
        tamano = tamanoTranslator(tamano)
        print("Que masa deseas:")
        printMasas()
        masa = input(">>> ")
        masa = masaTranslator(masa)
        print("Que salsa deseas:")
        printSalsas()
        salsa = input(">>> ")
        salsa = salsaTransator(salsa)
        print("Seleccione un total de tres ingredientes numéricamente.")       
        printIngredientes()
        print("\nPresione enter si desea no añadir mas ingredientes")
        ingredientes = []
        while(waiter.pizzaBuilder.checkMaxIngredientes(ingredientes)):
            ingrediente = input("\n>>> ")
            if(ingrediente == ""):
                break
            else:
                ingrediente = ingredienteTranslator(ingrediente)
                ingredientes.append(ingrediente)
        waiter.buildPizza(nombre,tamano,masa,salsa,ingredientes)
        print(waiter.getPizza().to_csv())
    else:
        #print("No has seleccionado una opcion válida")
        pass