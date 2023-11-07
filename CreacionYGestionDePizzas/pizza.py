import sys
sys.path.append('../')
from helpers import verificarMasa, verificarSalsa, verificarIngrediente, verificarTamano, verificarPizza
from config import TAMANOS , MASAS , SALSAS , INGREDIENTES

class Pizza:
    def __init__(self):
        self._tamano = ""
        self._masa = ""
        self._salsa = ""
        self._ingredientes = ""

    @property
    def tamano(self):
        return self._tamano
    
    @tamano.setter
    def tamano(self, tamano):
        if verificarTamano(TAMANOS,tamano):
            self._tamano = tamano
        else:
            raise ValueError("El tamaño no es correcto")

    @property
    def masa(self):
        return self._masa
    
    @masa.setter
    def masa(self, masa):
        if verificarMasa(MASAS,masa):
            self._masa = masa
        else:
            raise ValueError("La masa no es correcta")

    @property
    def salsa(self):
        return self._salsa
    
    @salsa.setter
    def salsa(self, salsa):
        if verificarSalsa(SALSAS,salsa):
            self._salsa = salsa
        else:
            raise ValueError("La salsa no es correcta")

    @property
    def ingredientes(self):
        return self._ingredientes
    
    @ingredientes.setter
    def ingredientes(self, ingredientes):
        for ingrediente in ingredientes:
            if not verificarIngrediente(INGREDIENTES,ingrediente):
                raise ValueError(f"El ingrediente {ingrediente} no es correcto")
        self._ingredientes = ingredientes
    def __str__(self):
        return f"masa: {self.masa}\nsalsa: {self.salsa}\ningredientes: {self.ingredientes}"