import pandas as pd
from abc import ABC, abstractmethod

# Definir las clases base de productos
class Estadistico(ABC):
    @abstractmethod
    def calcular(self, data):
        pass

class Grafico(ABC):
    @abstractmethod
    def dibujar(self, data):
        pass

# Productos concretos para análisis estadísticos
class Media(Estadistico):
    def calcular(self, data):
        return data.mean()

class Mediana(Estadistico):
    def calcular(self, data):
        return data.median()

class Moda(Estadistico):
    def calcular(self, data):
        return data.mode().iloc[0]

# Productos concretos para visualizaciones
class Histograma(Grafico):
    def dibujar(self, data):
        import matplotlib.pyplot as plt
        plt.hist(data, bins=10)
        plt.title('Histograma')
        plt.show()

class GraficoBarras(Grafico):
    def dibujar(self, data):
        import matplotlib.pyplot as plt
        data.plot(kind='bar')
        plt.title('Gráfico de Barras')
        plt.show()

# Fábricas abstractas
class FabricaAnalisis(ABC):
    @abstractmethod
    def crear_estadistico(self):
        pass

class FabricaVisualizacion(ABC):
    @abstractmethod
    def crear_grafico(self):
        pass

# Fábricas concretas que implementan las fábricas abstractas
class FabricaEstadisticos(FabricaAnalisis):
    def crear_estadistico(self, tipo):
        if tipo == 'media':
            return Media()
        elif tipo == 'mediana':
            return Mediana()
        elif tipo == 'moda':
            return Moda()
        else:
            raise ValueError(f'Tipo de estadístico no válido: {tipo}')

class FabricaVisualizaciones(FabricaVisualizacion):
    def crear_grafico(self, tipo):
        if tipo == 'histograma':
            return Histograma()
        elif tipo == 'grafico_barras':
            return GraficoBarras()
        else:
            raise ValueError(f'Tipo de gráfico no válido: {tipo}')


if __name__ == "__main__":
    # Carga de datos desde el archivo CSV
    file_path = "AnalisisModular/data/activaciones_samur_2023_clean.csv"
    data = pd.read_csv(file_path)


    fabrica_estadisticos = FabricaEstadisticos()
    estadistico_media = fabrica_estadisticos.crear_estadistico('media')
    resultado_media = estadistico_media.calcular(data)
    print("Media:", resultado_media)

    fabrica_visualizaciones = FabricaVisualizaciones()
    grafico_barras = fabrica_visualizaciones.crear_grafico('grafico_barras')
    grafico_barras.dibujar(data)

