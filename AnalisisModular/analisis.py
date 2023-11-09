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

def plotNulls(dataframe):
    dataframe.isnull().sum().plot(kind = "bar")
    plt.show();

def mainSAMUR():
    df = pd.read_csv(RUTA, sep = ";")
    print(df.info())
    df["MesToNumber"] = df["Mes"].apply(mesToNumber)
    modaMeses = getMode(df,"MesToNumber")
    print("El mes con más intervenciones es {}".format(numberToMes(modaMeses)))
    numerico = horaToNumber("0:01:36")
    desnumerico = numberToHora(numerico)
    print("\nPasamos a numérico la hora 0:01:36 --> {}".format(numerico))
    print("Hacemos la desconversion de {} --> {}".format(numerico,desnumerico))
    plotNulls(df)
    

if __name__ == '__main__':
    mainSAMUR()