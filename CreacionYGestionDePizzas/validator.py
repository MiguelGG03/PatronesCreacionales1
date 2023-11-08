from abc import ABC, abstractmethod
import csv
from config import CARTA_PATH, INGREDIENTES , SALSAS , MASAS , TAMANOS

class Validador(ABC):

    @abstractmethod
    def validar(self,*args,**kwargs):
        pass

class ValidarNombre(Validador):
    """
    Valida que el nombre de la pizza seleccionada exista dentro de la carta
    """

    def validar(self,nombre):
        with open(CARTA_PATH, newline='') as File:  
            reader = csv.reader(File,delimiter=';')
            for row in reader:
                if row[0] == nombre:
                    return True
            return False
class ValidarNombrePersonalizado(Validador):
    """
    Validar el nombre de la pizza personalizada
    """
    def validar(self,nombre):
        if(len(nombre)>=4 and len(nombre)<=16):
            return True
        return False
    
class ValidarIngredientes(Validador):
    """
    Valida que los ingredientes sean validos
    """
    def validar(self,ingredientes):
        for _ingrediente in ingredientes:
            if not (_ingrediente.lower() in INGREDIENTES):
                return False
        return True

class ValidarSalsas(Validador):
    """
    Valida que la salsa sea valida
    """
    def validar(self,salsa):
        for _salsa in SALSAS:
            if _salsa == salsa:
                return True
        return False

class ValidarMasas(Validador):
    """
    Valida que la salsa sea valida 
    """
    def validar(self,masa):
        for _masa in MASAS:
            if _masa == masa:
                return True
        return False

class ValidarTamano(Validador):
    """
    Valida que el tamaño sea valido
    """
    def validar(self,tamaño):
        for _tamaño in TAMANOS:
            if _tamaño == tamaño:
                return True
        return False

class ValidarPrecio(Validador):
    """
    Valida que el precio sea mayor (o igual en caso de descuento) que cero
    """
    def validar(self,precio):
        if(precio>=0.0):
            return True
        else:
            return False