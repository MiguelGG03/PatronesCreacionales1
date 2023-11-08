from abc import ABC, abstractmethod
import sys
sys.path.append('../')
from pizza import Pizza
from validator import *

class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = Pizza()

    @abstractmethod
    def setNombre(self,nombre):
        pass

    def setTamano(self, tamano):
        if (ValidarTamano().validar(tamano.lower())):
            self.pizza.tamano = tamano
        else:
            raise ValueError(f'El tamaño "{tamano}" no es válido')

    def setMasa(self, masa):
        if (ValidarMasas().validar(masa.lower())):
            self.pizza.masa = masa
        else:
            raise ValueError(f'La masa "{masa}" no es válida.')

    def setSalsa(self, salsa):
        if (ValidarSalsas().validar(salsa.lower())):
            self.pizza.salsa = salsa
        else:
            raise ValueError(f'La salsa "{salsa}" no es válida.')

    def setIngrediente(self, ingredientes:list[str]):
        if (ValidarIngredientes().validar(ingredientes)):
            self.pizza.ingredientes = ingredientes
        else:
            raise ValueError(f'Alguno de los ingredientes en {ingredientes} no es/son válido/s.')

    @abstractmethod
    def build(self,*args,**kwargs):
        pass

    def getPizza(self):
        return self.pizza

class CuatroQuesosPizzaBuilder(PizzaBuilder):
    def __init__(self):
        super().__init__()

    def setNombre(self,nombre):
        if(ValidarNombre().validar(nombre)):
            self.pizza.nombre = nombre
        else:
            raise ValueError(f'El nombre "{nombre}" no es válido.')


    def build(self,tamano,masa):
        self.setNombre("Cuatro Quesos")
        self.setTamano(tamano)
        self.setMasa(masa)
        self.setSalsa("tomate")
        self.setIngrediente(["mozzarella", "parmesano", "gorgonzola", "provolone"])

class MargaritaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        super().__init__()

    def setNombre(self,nombre):
        if(ValidarNombre().validar(nombre)):
            self.pizza.nombre = nombre
        else:
            raise ValueError(f'El nombre "{nombre}" no es válido.')

    def build(self,tamano,masa):
        self.setNombre("Margarita")
        self.setTamano(tamano)
        self.setMasa(masa)
        self.setSalsa("tomate")
        self.setIngrediente(["mozzarella, tomate, albahaca"])

class BarbacoaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        super().__init__()

    def setNombre(self,nombre):
        if(ValidarNombre().validar(nombre)):
            self.pizza.nombre = nombre
        else:
            raise ValueError(f'El nombre "{nombre}" no es válido.')

    def build(self,tamano,masa):
        self.setTamano(tamano)
        self.setMasa(masa)
        self.setSalsa("barbacoa")
        self.setIngrediente(["mozzarella", "carne", "bacon"])

class PersonalizadaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        super().__init__()

    def setNombre(self,nombre):
        if(ValidarNombrePersonalizado().validar(nombre)):
            self.pizza.nombre = nombre
        else:
            raise ValueError(f'El nombre "{nombre}" no es válido.\nDebe tener entre 4 y 16 caracteres')
    
    def checkMaxIngredientes(self,lista):
        """Por ahora hay un máximo de 3 ingredientes"""
        if(len(lista)<=3):
            return True
        else:
            print("No puedes añadir mas de tres ingredientes")
            return False

    def añadirIngredientes(self):
        ingredientes= []
        print
        return ingredientes

    def build(self,nombre,tamano,masa,salsa,ingredientes):
        self.setNombre(nombre)
        self.setTamano(tamano)
        self.setSalsa(masa)
        self.setSalsa(salsa)
        self.setIngrediente([])

if __name__ == '__main__':
    print(type(CuatroQuesosPizzaBuilder()))