import sys
sys.path.append('../')
from config import INGREDIENTES , SALSAS , TAMANOS , MASAS

def printSalsas():
    contador = 1
    print("Las salsas disponibles en la carta son:")
    for _ in SALSAS:
        print(f"{contador}. {_}")
        contador+=1

def printMasas():
    contador=1
    print("Las masas disponibles en la carta son:")
    for _ in MASAS:
        print(f"{contador}. {_}")
        contador+=1

def printTamanos():
    contador=1
    print("Los tamaños disponibles en la carta son:")
    for _ in TAMANOS:
        print(f"{contador}. {_}")
        contador+=1

def printIngredientes():
    contador=1
    print("Los Ingredientes disponibles en la carta son:")
    for _ in INGREDIENTES:
        print(f"{contador}. {_}")
        contador+=1