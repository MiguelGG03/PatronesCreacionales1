import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("../")
from helpers import *
from config import RUTA


def limpieza():
    df = pd.read_csv(RUTA, sep = ";")
    originalLEN = df.shape
    #plotNulos(df)
    print('Tenemos un total de {} hspitales desconocidos.\nCambiamos sus valores por "Desconocido"'.format(df["Hospital"].isnull().sum()))
    df["Hospital"].fillna("Desconocido", inplace = True)
    print('Vamos a comprobar que otras columnas tienen nulos:\n')
    comprobarNulos(df)
    print("\nComo podemos ver sigue habiendo nulos")
    print("Lo que nos interesa es dropear las filas\n"
          "que tengan nulo tanto en la hora de solicitud\n"
          "como en la de intervención, porque no aportan nada\n"
          "y a lo sumo son 1107.\n"
          "El resto de valores se rellenaran con un 'Desconocido'.")
    
    columns_to_check = ["Hora Solicitud", "Hora Intervencion"]
    limpiarNulos(df, columns_to_check)
    noNullLEN = df.shape
    columns_to_check = ["Código","Distrito"]
    limpiarNulos(df, columns_to_check)
    df.fillna("Desconocido", inplace = True)
    print("Vamos a comprobar que no hay nulos")
    comprobarNulos(df)
    #plotNulos(df)
    print()
    print("Los datos sin limpiar : {}".format(originalLEN))
    print("Los datos limpios : {}".format(noNullLEN))
    print("Hemos eliminado {} filas".format(originalLEN[0] - noNullLEN[0]))
    print("\nVamos a trabajar con estos datos ya limpiados")
    print()
    df["MesToNumber"] = df["Mes"].apply(mesToNumber)
    modaMeses = getMode(df,"MesToNumber")
    print("El mes con más intervenciones es {}".format(numberToMes(modaMeses)))
    print("Originalmente era JULIO pero limpiar los datos lo ha cambiado")
    print()
    print("En media se opera en el mes {} \nEsto equivale a {}".format(df["MesToNumber"].mean(),numberToMes(round(df["MesToNumber"].mean(),0))))
    print()
    print('Ahora veamos a que hora se suele intervenir en media.')
    print('Miramos la media y no la moda porque no vamos a contrar\n2 iguales.')
    print()
    df["HoraSolicitudToNumber"] = df["Hora Solicitud"].apply(horaToNumber) 
    print('En media se opera a las {}, que esto equivale a las {}'.format(df["HoraSolicitudToNumber"].mean(),numberToHora(df["HoraSolicitudToNumber"].mean())))
    print()
    print("Guardo el csv y lo uso en el AbstractFactory")
    df.to_csv("AnalisisModular/data/activaciones_samur_2023_clean.csv", sep = ";", index = False)




if __name__ == '__main__':
    limpieza()