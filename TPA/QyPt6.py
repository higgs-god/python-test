from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.boton = QPushButton("Presioname", self)
        self.boton.setGeometry(100, 100, 100, 50)

app = QApplication(sys.argv)
ventana_principal = VentanaPrincipal()
ventana_principal.show()
sys.exit(app.exec())
      
