import csv
import os

def verificarPizza(pizza):
    # Construir la ruta al archivo csv
    RUTA = os.path.join(".", "CreacionYGestionDePizzas", "carta.csv")
    with open(RUTA, newline='') as File:  
        reader = csv.reader(File,delimiter=';')
        for row in reader:
            if row[0] == pizza:
                return True
        return False

def verificarIngrediente(lista,ingrediente):
    for algo in lista:
        if algo == ingrediente:
            return True
    return False

if __name__ == "__main__":
    print(verificarPizza("Margarita"))
    print(verificarIngrediente(["queso","tomate"],"queso"))