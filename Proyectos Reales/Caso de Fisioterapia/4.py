# Fisioterapia Andy


# Mostrar el menú principal
def menu():
    print("")
    print("-------- Bienvenidos a PhysioKinect --------")
    print("     Fisioterapia deportiva y traumatológica")
    print("")
    print("1. Registrar nuevo paciente")
    print("2. Agendar cita")
    print("3. Calcular costo de la cita")
    print("4. Salir")


# Función para registrar un nuevo paciente
def registrar_paciente(pacientes):
    print("\n--- Registrar nuevo paciente ---")
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    telefono = input("Ingrese el teléfono del paciente: ")
    correo = input("Ingrese el correo del paciente: ")
    observaciones = input("Observaciones sobre el paciente: ")
    # Guardar paciente en la lista
    pacientes.append(
        {
            "nombre": nombre,
            "edad": edad,
            "telefono": telefono,
            "correo": correo,
            "observaciones": observaciones,
        }
    )
    print(f"Paciente {nombre} registrado con éxito.")


# Función para agendar una cita
def agendar_cita(citas):
    print("\n--- Agendar cita ---")
    nombre = input("Ingrese el nombre del paciente: ")
    servicio = input(
        "Servicio solicitado (Masaje/Revisión/Traumatología): "
    ).capitalize()
    fecha_cita = input("Ingrese la fecha de la cita (DD/MM/AA): ")
    hora_cita = input("Ingrese la hora de la cita (HH:MM): ")
    # Guardar cita en la lista
    citas.append(
        {"nombre": nombre, "servicio": servicio, "fecha": fecha_cita, "hora": hora_cita}
    )
    print(f"Cita agendada para {nombre} el {fecha_cita} a las {hora_cita}.")


# Función para calcular el costo de una cita
def calcular_costo():
    print("\n--- Calcular costo de la cita ---")
    print("1. Masaje ($30 por sesión)")
    print("2. Revisión ($20 por sesión)")
    print("3. Traumatología ($40 por sesión)")

    # Seleccionar servicio
    servicio = int(input("Seleccione el servicio (1-3): "))
    if servicio == 1:
        precio = 30
        nombre_servicio = "Masaje"
    elif servicio == 2:
        precio = 20
        nombre_servicio = "Revisión"
    elif servicio == 3:
        precio = 40
        nombre_servicio = "Traumatología"
    else:
        print("Opción no válida.")
        return

    # Calcular costo total
    sesiones = int(input("Ingrese el número de sesiones: "))
    total = precio * sesiones
    print(f"\nServicio seleccionado: {nombre_servicio}")
    print(f"Número de sesiones: {sesiones}")
    print(f"Costo total: ${total}")


# Listas para almacenar pacientes y citas
pacientes = []
citas = []

# Bucle principal del programa
while True:
    menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        registrar_paciente(pacientes)
    elif opcion == "2":
        agendar_cita(citas)
    elif opcion == "3":
        calcular_costo()
    elif opcion == "4":
        print("Gracias por usar PhysioKinect. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")
