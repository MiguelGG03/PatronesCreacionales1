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
    print("Vamos a ver que fabrica de estadisticos quieres usar")
    print("1. Media")
    print("2. Mediana")
    print("3. Moda")
    print("4. Salir")
    print()
    opcion = (input(">>> "))
    opcion = traductorEstadisticaFactory(opcion)
    if opcion == None:
        print("Cerrando programa")
        exit()
    else:
        estadistico = fabrica_estadisticos.crear_estadistico(opcion)
        resultado = estadistico.calcular(dataframe)
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
