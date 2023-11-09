import sys
import matplotlib.pyplot as plt
sys.path.append("../")
from config import MESES_TO_NUMBERS , NUMBERS_TO_MESES

def mesToNumber(mes):
    mes_en_mayusculas = mes.upper()
    
    if mes_en_mayusculas in MESES_TO_NUMBERS:
        return MESES_TO_NUMBERS[mes_en_mayusculas]
    else:
        return None


def numberToMes(number):    
    if number in NUMBERS_TO_MESES:
        return NUMBERS_TO_MESES[number]
    else:
        return None


def getMode(dataframe,column):
    value_counts = dataframe[column].value_counts()
    value = value_counts.idxmax()
    return value


def horaToNumber(tiempo):
    horas, minutos, segundos = map(int, tiempo.split(':'))
    
    tiempo_en_horas = horas + minutos / 60 + segundos / 3600
    return tiempo_en_horas


def numberToHora(tiempo):
    horas = int(tiempo)
    minutos = int((tiempo - horas) * 60)
    segundos = int((tiempo - horas - minutos / 60) * 3600)
    
    return "{}:{}:{}".format(horas, minutos, segundos)


def plotNulos(dataframe):
    dataframe.isnull().sum().plot(kind = "bar")
    plt.show();


def comprobarNulos(dataframe):
    for column in dataframe.columns:
        if (dataframe[column].isnull().sum() > 0):
            print('{} : {} nulos'.format(column,dataframe[column].isnull().sum()))   


def limpiarNulos(dataframe, columns_to_check):

    if all(item in dataframe.columns for item in columns_to_check):
        dataframe.dropna(subset = columns_to_check, inplace = True)
    else:
        missing_cols = [col for col in columns_to_check if col not in dataframe.columns] 
        print(f"Missing columns: {missing_cols}")


def traductorEstadisticaFactory(opcion):
    if opcion == '1':
        return 'media'
    elif opcion == '2':
        return 'mediana'
    elif opcion == '3':
        return 'moda'
    else:
        return None
    

def traductorGraficoFactory(opcion):
    if opcion == '1':
        return 'histograma'
    elif opcion == '2':
        return 'grafico de barras'
    else:
        return None