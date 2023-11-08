import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
                             QLabel, QComboBox, QLineEdit, QMessageBox, QFormLayout, QCheckBox)
sys.path.append("../")
from CSVstorage import CSVstorage
from waiter import Waiter
from pizzaBuilder import *
from config import PEDIDOS_PATH, TAMANOS, MASAS, INGREDIENTES, SALSAS

class PizzaOrderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.storage = CSVstorage(PEDIDOS_PATH)
        self.waiter = Waiter()
        self.selected_ingredients = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pizza Builder App')
        self.setGeometry(100, 100, 800, 600)
        layout = QVBoxLayout()

        self.pizza_combo = QComboBox()
        self.pizza_combo.addItems(["Cuatro Quesos", "Barbacoa", "Margarita", "Personalizada"])
        self.pizza_combo.currentIndexChanged.connect(self.toggle_personalized_options)
        layout.addWidget(self.pizza_combo)

        self.size_combo = QComboBox()
        self.size_combo.addItems(TAMANOS)
        layout.addWidget(self.size_combo)

        self.dough_combo = QComboBox()
        self.dough_combo.addItems(MASAS)
        layout.addWidget(self.dough_combo)

        self.create_personalized_options(layout)

        self.order_button = QPushButton('Hacer pedido')
        self.order_button.clicked.connect(self.place_order)
        layout.addWidget(self.order_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setStyleSheet("""
    QMainWindow {
        background-image: url('images/interior.png');
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: scroll;
        background-size: cover;
    }
    QPushButton {
        font: bold;
        background-color: #DAA520;  /* Dorado */
        border-radius: 10px;
        padding: 10px;
    }
    QPushButton:hover {
        background-color: #F0E68C;  /* Khaki claro para efecto hover */
    }
    QLabel, QComboBox, QLineEdit {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 16px;
    }
    QComboBox {
        background-color: #FFF8DC;  /* Un color crema que combina bien con el amarillo */
        color: #8B4513;  /* Marrón oscuro para el texto */
        border-radius: 5px;
        padding: 5px;
        border: 1px solid #DAA520;
    }
    QLineEdit {
        background-color: white;
        border: 1px solid #DAA520;  /* Borde dorado */
    }
    """)

    def create_personalized_options(self, layout):
        self.personalized_layout = QFormLayout()
        self.pizza_name_input = QLineEdit()
        self.pizza_name_input.setPlaceholderText("Nombre de la pizza (4-16 caracteres)")
        self.personalized_layout.addRow("Nombre:", self.pizza_name_input)

        for ingrediente in INGREDIENTES:
            cb = QCheckBox(ingrediente)
            cb.stateChanged.connect(self.update_ingredient_selection)
            self.personalized_layout.addRow(cb)

        self.sauce_combo = QComboBox()
        self.sauce_combo.addItems(SALSAS)
        self.personalized_layout.addRow("Salsas:", self.sauce_combo)

        self.personalized_options = QWidget()
        self.personalized_options.setLayout(self.personalized_layout)
        self.personalized_options.setVisible(False)
        layout.addWidget(self.personalized_options)

    def toggle_personalized_options(self, index):
        is_personalized = self.pizza_combo.currentText() == "Personalizada"
        self.personalized_options.setVisible(is_personalized)

    def update_ingredient_selection(self, state):
        source = self.sender()
        if state == Qt.Checked and len(self.selected_ingredients) < 3:
            self.selected_ingredients.append(source.text())
        elif state == Qt.Unchecked and source.text() in self.selected_ingredients:
            self.selected_ingredients.remove(source.text())
        else:
            source.setChecked(False)
            QMessageBox.warning(self, 'Advertencia', 'Solo puedes seleccionar hasta 3 ingredientes.')

    def place_order(self):
        pizza_type = self.pizza_combo.currentText()
        pizza_size = self.size_combo.currentText()
        pizza_dough = self.dough_combo.currentText()
        if pizza_type == "Cuatro Quesos":
            self.waiter.pizzaBuilder = CuatroQuesosPizzaBuilder()
        elif pizza_type == "Barbacoa":
            self.waiter.pizzaBuilder = BarbacoaPizzaBuilder()
        # ... etc ...

        if pizza_type == "Personalizada":
            pizza_name = self.pizza_name_input.text()
            if not (4 <= len(pizza_name) <= 16):
                QMessageBox.warning(self, 'Error', 'El nombre de la pizza debe tener entre 4 y 16 caracteres.')
                return
            if len(self.selected_ingredients) == 0:
                QMessageBox.warning(self, 'Error', 'Debes seleccionar al menos un ingrediente.')
                return
            sauce = self.sauce_combo.currentText()
            self.waiter.pizzaBuilder = PersonalizadaPizzaBuilder()
            self.waiter.buildPizza(pizza_name, pizza_size, pizza_dough, sauce, self.selected_ingredients)
        else:
            self.waiter.buildPizza(pizza_size, pizza_dough)

        pizza = self.waiter.getPizza()
        data = self.storage.load()
        data.append(pizza.to_csv())
        self.storage.save(data)
        QMessageBox.information(self, 'Pedido', 'Tu pizza ha sido pedida con éxito!')

def ui():
    app = QApplication(sys.argv)
    main_window = PizzaOrderApp()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    ui()
