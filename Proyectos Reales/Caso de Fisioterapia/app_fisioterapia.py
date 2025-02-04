import tkinter as tk
from tkinter import messagebox, ttk


def menu():
    print("Bienvenidos al sistema de fisioterapia")
    print("1. Registrar un nuevo paciente")
    print("2. Agendar una cita")
    print("3. Calcular costo de las sesiones")
    print("4. Salir")


def registrar_paciente(pacientes):
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese su edad: "))
    telefono = int(input("Ingrese su numero personal"))
    pacientes.append({"nombre": nombre, "edad": edad, "telefono": telefono})
    print(f"Paciente {nombre} registrado exitosamente.")


def agendar_cita(citas):
    nombre = input("Ingrese el nombre del paciente: ").strip()
    fecha = input("Ingrese la fecha de la cita (DD/MM/AAAA): ").strip()
    hora = input("Ingrese la hora de la cita (HH:MM): ").strip()
    citas.append({"nombre": nombre, "fecha": fecha, "hora": hora})
    print(f"Cita para {nombre} agendada exitosamente el {fecha} a las {hora}.")


def calcular_costo():
    costo_por_sesion = 50  # Puedes cambiar este valor
    sesiones = int(input("Ingrese la cantidad de sesiones que realizará el paciente: "))
    total = costo_por_sesion * sesiones
    print(f"El costo total por {sesiones} sesiones es: ${total}")


def registrar_paciente_gui():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    telefono = entry_telefono.get()

    if nombre and edad and telefono:
        pacientes.append({"nombre": nombre, "edad": edad, "telefono": telefono})
        messagebox.showinfo(
            "Registro Exitoso", f"Paciente {nombre} registrado exitosamente."
        )
    else:
        messagebox.showwarning("Faltan datos", "Por favor, ingrese todos los campos.")


# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Fisioterapia")
root.geometry("500x400")
root.config(bg="lightblue")  # Fondo de la ventana

# Crear un Frame para organizar los widgets
frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=20)

# Personalización de la etiqueta y campo de entrada para el nombre
label_nombre = tk.Label(
    frame, text="Nombre del paciente:", font=("Arial", 12), bg="lightblue"
)
label_nombre.grid(row=0, column=0, padx=10, pady=5)

entry_nombre = tk.Entry(frame, font=("Arial", 12), fg="black", bg="lightyellow")
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

# Personalización de la etiqueta y campo de entrada para la edad
label_edad = tk.Label(frame, text="Edad:", font=("Arial", 12), bg="lightblue")
label_edad.grid(row=1, column=0, padx=10, pady=5)

entry_edad = tk.Entry(frame, font=("Arial", 12), fg="black", bg="lightyellow")
entry_edad.grid(row=1, column=1, padx=10, pady=5)

# Personalización de la etiqueta y campo de entrada para el teléfono
label_telefono = tk.Label(frame, text="Teléfono:", font=("Arial", 12), bg="lightblue")
label_telefono.grid(row=2, column=0, padx=10, pady=5)

entry_telefono = tk.Entry(frame, font=("Arial", 12), fg="black", bg="lightyellow")
entry_telefono.grid(row=2, column=1, padx=10, pady=5)

# Botón para registrar paciente
button_registrar = tk.Button(
    frame,
    text="Registrar Paciente",
    command=registrar_paciente_gui,
    font=("Arial", 12),
    fg="white",
    bg="green",
)
button_registrar.grid(row=3, columnspan=2, pady=10)

# Menú en el terminal
menu()

# Bucle principal
pacientes = []
citas = []

while True:
    opcion = input("Seleccione una opción (1-4): ").strip()

    if opcion == "1":
        registrar_paciente(pacientes)
    elif opcion == "2":
        agendar_cita(citas)
    elif opcion == "3":
        calcular_costo()
    elif opcion == "4":
        print("¡Gracias por usar el sistema! Hasta pronto.")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")

root.mainloop()
