from abc import ABC, abstractmethod
import sys
sys.path.append('../')
from pizza import Pizza

class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = Pizza()

    def setTamano(self, tamano):
        self.pizza.tamano = tamano

    def setMasa(self, masa):
        self.pizza.masa = masa

    def setSalsa(self, sauce):
        self.pizza.salsa = sauce

    def setIngrediente(self, ingredientes:list[str]):
        self.pizza.ingredientes = ingredientes

    @abstractmethod
    def build(self):
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