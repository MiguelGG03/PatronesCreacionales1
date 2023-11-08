from abc import ABC, abstractmethod
import sys
sys.path.append('../')
from pizza import Pizza
from validator import *

class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = Pizza()

    def setNombre(self,nombre):
        if(ValidarNombre().validar(nombre)):
            self.pizza.nombre = nombre
        else:
            raise ValueError(f'El tamaño "{nombre}" no es valido')

    def setTamano(self, tamano):
        if (ValidarTamano().validar(tamano.lower())):
            self.pizza.tamano = tamano
        else:
            raise ValueError(f'El tamaño "{tamano}" no es valido')

    def setMasa(self, masa):
        if (ValidarMasas().validar(masa.lower())):
            self.pizza.masa = masa
        else:
            raise ValueError(f'La masa "{masa}" no es valida')

    def setSalsa(self, salsa):
        if (ValidarSalsas().validar(salsa.lower())):
            self.pizza.salsa = salsa
        else:
            raise ValueError(f'La salsa "{salsa}" no es valida')

    def setIngrediente(self, ingredientes:list[str]):
        if (ValidarIngredientes().validar(ingredientes)):
            self.pizza.ingredientes = ingredientes
        else:
            raise ValueError(f'Alguno de los ingredientes en {ingredientes} no es/son valido/s')

    @abstractmethod
    def build(self,*args,**kwargs):
        pass

    def getPizza(self):
        return self.pizza

class CuatroQuesosPizzaBuilder(PizzaBuilder):
    def __init__(self):
        super().__init__()

    def build(self):
        self.setTamano("Mediana")
        self.setMasa("Crujiente")
        self.setSalsa("Tomate")
        self.setIngrediente(["Mozzarella", "Gorgonzola", "Parmesano", "Queso de cabra"])

class MargaritaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        super().__init__()

    def build(self):
        self.setTamano("Pequena")
        self.setMasa("Fina")
        self.setSalsa("Tomate")
        self.setIngrediente(["Mozzarella, Tomate, Albahaca"])

class BarbacoaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        super().__init__()

    def build(self):
        self.setTamano("Familiar")
        self.setMasa("Gorda")
        self.setSalsa("Barbacoa")
        self.setIngrediente(["Mozzarella", "Carne", "Bacon"])

class PersonalizadaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        super().__init__()
    
    def checkMaxIngredientes(self,lista):
        if(len(lista)<=3):
            return True
        else:
            raise ValueError("No puedes añadir mas de 3 ingredientes")

    def build(self):
        self.setTamano("")
        self.setSalsa("")
        self.setSalsa("")
        self.setIngrediente([])