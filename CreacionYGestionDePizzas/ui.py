import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QComboBox, QLineEdit

class PizzaOrderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pizza Builder App')
        self.setGeometry(100, 100, 800, 600)

        # Layout principal
        layout = QVBoxLayout()

        # Etiqueta de bienvenida
        welcome_label = QLabel("Buenas!\nQue pizza vas a desear tomar?")
        layout.addWidget(welcome_label)

        # Selector de pizza
        self.pizza_combo = QComboBox()
        self.pizza_combo.addItems(["Cuatro Quesos", "Barbacoa", "Margarita", "Personalizada"])
        layout.addWidget(self.pizza_combo)

        # Botón para confirmar selección
        self.order_button = QPushButton('Ordenar')
        self.order_button.clicked.connect(self.place_order)
        layout.addWidget(self.order_button)

        # Configurar el widget central con el layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def place_order(self):
        # Obtener la selección del usuario
        pizza_choice = self.pizza_combo.currentText()
        # Aquí conectarías con la lógica de tu pedido de pizza
        print(f"Has seleccionado: {pizza_choice}")
        # ... continuar con la lógica de pedido ...

def ui():
    app = QApplication(sys.argv)
    main_window = PizzaOrderApp()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    ui()
