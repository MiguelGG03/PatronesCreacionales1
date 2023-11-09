import sys
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
