import sys
sys.path.append('../')
from pizza import Pizza

class PizzaBuilder:
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