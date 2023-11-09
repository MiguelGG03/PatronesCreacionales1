import pandas as pd
import sys
sys.path.append("../")
from config import RUTA_CLEAN
from abstractFactory import *
from helpers import traductorEstadisticaFactory, traductorGraficoFactory

def main():
    dataframe = pd.read_csv(RUTA_CLEAN, sep = ";")
    fabrica_estadisticos = FabricaEstadisticos()
    fabrica_visualizaciones = FabricaVisualizaciones()
    print("Bienvenido al programa de analisis modular")
    print()
    print("Que columna del dataset deseas analizar?")
    contador = 1
    # seleccionar columnas numéricas


    for column in dataframe.columns:
        print( str(contador) + ". "+column)
        contador += 1
    print()
    opcion = (input(">>> "))
    columna = dataframe[int(opcion)-1]
    print(columna)
    columna = columna.apply(pd.to_numeric, errors='coerce')
    print("Has elegido la columna {}".format(opcion))
    print()
    print("Vamos a ver que fabrica de estadisticos quieres usar")
    print("1. Media")
    print("2. Mediana")
    print("3. Moda")
    print()
    opcion = (input(">>> "))
    opcion = traductorEstadisticaFactory(opcion)
    if opcion == None:
        print("Cerrando programa")
        exit()
    else:
        estadistico = fabrica_estadisticos.crear_estadistico(opcion)
        resultado = estadistico.calcular(columna)
        print("El resultado es {}".format(resultado))
        print()
        print("Vamos a ver que fabrica de graficos quieres usar")
        print("1. Histograma")
        print("2. Grafico de barras")
        print("3. Salir")
        print()
        opcion = (input(">>> "))
        opcion = traductorGraficoFactory(opcion)
        if opcion == 'salir':
            print("Adios")
            exit()
        else:
            grafico = fabrica_visualizaciones.crear_grafico(opcion)
            grafico.dibujar(dataframe)

if __name__ == '__main__':
    main()