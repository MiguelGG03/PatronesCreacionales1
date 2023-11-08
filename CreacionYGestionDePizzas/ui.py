import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
                             QLabel, QComboBox, QLineEdit, QMessageBox, QFormLayout, QSpinBox)
sys.path.append("../")
from CSVstorage import CSVstorage  # Asegúrate de que esta clase tenga métodos load() y save()
from waiter import Waiter
from pizzaBuilder import *
from config import PEDIDOS_PATH, TAMANOS, MASAS, INGREDIENTES, SALSAS  # Constantes definidas en config.py

class PizzaOrderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.storage = CSVstorage(PEDIDOS_PATH)
        self.waiter = Waiter()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pizza Builder App')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Selector de pizza
        self.pizza_combo = QComboBox()
        self.pizza_combo.addItems(["Cuatro Quesos", "Barbacoa", "Margarita", "Personalizada"])
        self.pizza_combo.currentIndexChanged.connect(self.toggle_personalized_options)
        layout.addWidget(self.pizza_combo)

        # Campos para la pizza personalizada
        self.personalized_layout = QFormLayout()

        # Campo para el nombre de la pizza
        self.pizza_name_input = QLineEdit()
        self.pizza_name_input.setPlaceholderText("Nombre de la pizza (4-16 caracteres)")
        self.personalized_layout.addRow("Nombre:", self.pizza_name_input)

        # Selector de ingredientes
        self.ingredients_combo = QComboBox()
        self.ingredients_combo.addItems(INGREDIENTES)
        self.selected_ingredients = []
        self.ingredients_combo.currentIndexChanged.connect(self.add_ingredient)
        self.personalized_layout.addRow("Ingredientes:", self.ingredients_combo)

        # Contador de ingredientes seleccionados
        self.ingredients_count = QSpinBox()
        self.ingredients_count.setRange(0, 3)
        self.ingredients_count.setReadOnly(True)
        self.personalized_layout.addRow("Seleccionados:", self.ingredients_count)

        # Selector de salsas
        self.sauce_combo = QComboBox()
        self.sauce_combo.addItems(SALSAS)
        self.personalized_layout.addRow("Salsas:", self.sauce_combo)

        # Inicialmente ocultar opciones personalizadas
        self.personalized_options = QWidget()
        self.personalized_options.setLayout(self.personalized_layout)
        self.personalized_options.setVisible(False)
        layout.addWidget(self.personalized_options)

        # Continuación de la UI...

    def toggle_personalized_options(self, index):
        # Mostrar u ocultar las opciones personalizadas según la selección
        is_personalized = self.pizza_combo.currentText() == "Personalizada"
        self.personalized_options.setVisible(is_personalized)

    def add_ingredient(self, index):
        ingredient = self.ingredients_combo.currentText()
        if ingredient not in self.selected_ingredients:
            if self.ingredients_count.value() < 3:
                self.selected_ingredients.append(ingredient)
                self.ingredients_count.setValue(self.ingredients_count.value() + 1)
            else:
                QMessageBox.warning(self, 'Advertencia', 'Solo puedes seleccionar hasta 3 ingredientes.')

    # Continuación de los métodos...

# Continuación de la aplicación...

    def place_order(self):
        # Obtener las selecciones del usuario
        pizza_type = self.pizza_combo.currentText()
        pizza_size = self.size_combo.currentText()
        pizza_dough = self.dough_combo.currentText()

        # Lógica para construir la pizza
        if pizza_type == "Cuatro Quesos":
            self.waiter.pizzaBuilder = CuatroQuesosPizzaBuilder()
        elif pizza_type == "Barbacoa":
            self.waiter.pizzaBuilder = BarbacoaPizzaBuilder()
        # ... etc ...

        # Aquí asumimos que la lógica de buildPizza ha sido adaptada para trabajar con PyQt
        self.waiter.buildPizza(pizza_size, pizza_dough)
        pizza = self.waiter.getPizza()

        # Guardar la pizza en la base de datos
        data = self.storage.load()
        data.append(pizza.to_csv())
        self.storage.save(data)

        # Confirmar el pedido al usuario
        QMessageBox.information(self, 'Pedido', 'Tu pizza ha sido pedida con éxito!')

def ui():
    app = QApplication(sys.argv)
    main_window = PizzaOrderApp()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    ui()
