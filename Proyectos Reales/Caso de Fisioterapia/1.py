import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QFormLayout,
    QHBoxLayout,
)


class FisioterapiaApp(QWidget):
    def __init__(self):
        super().__init__()

        # Inicializar la ventana
        self.setWindowTitle("Sistema de Fisioterapia")
        self.setGeometry(100, 100, 400, 300)

        # Layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Crear widgets
        self.init_ui()

    def init_ui(self):
        # Menú principal
        self.menu_label = QLabel("Bienvenidos al sistema de fisioterapia", self)
        self.layout.addWidget(self.menu_label)

        # Botones
        self.registrar_btn = QPushButton("Registrar un nuevo paciente", self)
        self.agendar_btn = QPushButton("Agendar una cita", self)
        self.calcular_btn = QPushButton("Calcular costo de las sesiones", self)
        self.salir_btn = QPushButton("Salir", self)

        # Conectar botones a funciones
        self.registrar_btn.clicked.connect(self.registrar_paciente)
        self.agendar_btn.clicked.connect(self.agendar_cita)
        self.calcular_btn.clicked.connect(self.calcular_costo)
        self.salir_btn.clicked.connect(self.salir)

        # Añadir botones al layout
        self.layout.addWidget(self.registrar_btn)
        self.layout.addWidget(self.agendar_btn)
        self.layout.addWidget(self.calcular_btn)
        self.layout.addWidget(self.salir_btn)

    def registrar_paciente(self):
        self.registrar_window = QWidget()
        self.registrar_window.setWindowTitle("Registrar Paciente")
        self.registrar_window.setGeometry(150, 150, 300, 200)

        form_layout = QFormLayout()

        self.nombre_input = QLineEdit()
        self.edad_input = QLineEdit()
        self.telefono_input = QLineEdit()

        form_layout.addRow("Nombre:", self.nombre_input)
        form_layout.addRow("Edad:", self.edad_input)
        form_layout.addRow("Teléfono:", self.telefono_input)

        submit_btn = QPushButton("Registrar", self)
        submit_btn.clicked.connect(self.submit_registro)

        form_layout.addWidget(submit_btn)

        self.registrar_window.setLayout(form_layout)
        self.registrar_window.show()

    def submit_registro(self):
        nombre = self.nombre_input.text()
        edad = self.edad_input.text()
        telefono = self.telefono_input.text()
        print(f"Paciente registrado: {nombre}, Edad: {edad}, Teléfono: {telefono}")
        self.registrar_window.close()

    def agendar_cita(self):
        self.agendar_window = QWidget()
        self.agendar_window.setWindowTitle("Agendar Cita")
        self.agendar_window.setGeometry(150, 150, 300, 200)

        form_layout = QFormLayout()

        self.paciente_input = QLineEdit()
        self.fecha_input = QLineEdit()
        self.hora_input = QLineEdit()

        form_layout.addRow("Paciente:", self.paciente_input)
        form_layout.addRow("Fecha (DD/MM/AAAA):", self.fecha_input)
        form_layout.addRow("Hora (HH:MM):", self.hora_input)

        submit_btn = QPushButton("Agendar Cita", self)
        submit_btn.clicked.connect(self.submit_agendar)

        form_layout.addWidget(submit_btn)

        self.agendar_window.setLayout(form_layout)
        self.agendar_window.show()

    def submit_agendar(self):
        paciente = self.paciente_input.text()
        fecha = self.fecha_input.text()
        hora = self.hora_input.text()
        print(f"Cita agendada para {paciente} el {fecha} a las {hora}")
        self.agendar_window.close()

    def calcular_costo(self):
        self.costo_window = QWidget()
        self.costo_window.setWindowTitle("Calcular Costo")
        self.costo_window.setGeometry(150, 150, 300, 200)

        form_layout = QFormLayout()

        self.sesiones_input = QLineEdit()

        form_layout.addRow("Cantidad de sesiones:", self.sesiones_input)

        submit_btn = QPushButton("Calcular", self)
        submit_btn.clicked.connect(self.submit_calcular)

        form_layout.addWidget(submit_btn)

        self.costo_window.setLayout(form_layout)
        self.costo_window.show()

    def submit_calcular(self):
        sesiones = self.sesiones_input.text()
        costo_por_sesion = 50
        total = int(sesiones) * costo_por_sesion
        print(f"El costo total por {sesiones} sesiones es: ${total}")
        self.costo_window.close()

    def salir(self):
        print("¡Gracias por usar el sistema! Hasta pronto.")
        self.close()


# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FisioterapiaApp()
    window.show()
    sys.exit(app.exec_())
