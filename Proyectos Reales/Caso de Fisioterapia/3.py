# Fisiterapia


def menu():
    print("Bienvenidos al sistema de fisioterapia")
    print("1.Registrar un nuevo paciente ")
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


pacientes = []
citas = []

# Bucle principal
while True:
    menu()
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
