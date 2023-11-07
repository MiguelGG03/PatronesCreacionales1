from abc import ABC, abstractmethod
import csv
from config import CARTA_PATH, INGREDIENTES , SALSAS

class Validador(ABC):

    @abstractmethod
    def validar(self,*args,**kwargs):
        pass

class ValidarPizza(Validador):

    def validar(self,pizza):
        with open(CARTA_PATH, newline='') as File:  
            reader = csv.reader(File,delimiter=';')
            for row in reader:
                if row[0] == pizza:
                    return True
            return False

class ValidarIngredientes(Validador):
    """
    Valida que los ingredientes sean validos
    """
    def validar(self,ingrediente):
        for _ingrediente in INGREDIENTES:
            if _ingrediente == ingrediente:
                return True
        return False

class ValidarSalsa(Validador):
    """
    Valida que la salsa sea valida
    """
    def validar(self,salsa):
        for _salsa in SALSAS:
            if _salsa == salsa:
                return True
        return False