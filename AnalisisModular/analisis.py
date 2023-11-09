# Derechos legales:
# https://datos.madrid.es/egob/catalogo/aviso-legal
# Condiciones a tener en cuenta:
"""
Estas son las condiciones de uso para la reutilización de documentos y datos del 
Ayuntamiento de Madrid:

· Obligatoriedad de las condiciones generales:
Cualquier persona o empresa que reutilice datos se ve obligada a cumplir estas condiciones.

· Autorización de reutilización y cesión de derechos de propiedad intelectual:
Se permite la reutilización de documentos y datos del Ayuntamiento de Madrid para usos comerciales
y no comerciales, abarcando actividades como copia, difusión, modificación, adaptación y combinación
de la información. Se cede una autorización gratuita y no exclusiva de los derechos de propiedad
intelectual.

· Condiciones generales para la reutilización:

- Prohibición de desnaturalizar la información.
- Debe citarse la fuente y la fecha de actualización de los documentos.
- No implicar la participación o respaldo del Ayuntamiento en la reutilización.
- Conservar los metadatos y está prohibido re-identificar información anonimizada.

· Exclusión de responsabilidad:

El uso de los conjuntos de datos se realiza bajo el propio riesgo del reutilizador. 
El Ayuntamiento de Madrid no se hace responsable de daños o pérdidas causadas directa o
indirectamente por la reutilización de la información.

· Responsabilidad del reutilizador:
El reutilizador debe cumplir con la normativa vigente sobre reutilización de información 
del sector público, incluyendo el régimen sancionador establecido por la ley.

En resumen, las condiciones generales exigen respeto por la información, atribución de la fuente 
y la fecha, prohíben desnaturalizar o reidentificar datos, y establecen la responsabilidad del 
reutilizador en cumplir con la normativa correspondiente, eximiendo de responsabilidad al Ayuntamiento 
por el uso de la información reutilizada.

Los datos se hacen referencia a las Activaciones del SAMUR-Protección Civil en el año 2023.
La ruta del archivo : AnalisisModular/data/activaciones_samur_2023.csv
"""
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("../")
from helpers import *
from config import RUTA


def mainSAMUR():
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
    print("Guardo el csv y lo uso en el abstAbstractFactory")




if __name__ == '__main__':
    mainSAMUR()