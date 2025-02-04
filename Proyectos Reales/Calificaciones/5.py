# Programa para registrar estudiantes y calificaciones

# Lista para almacenar estudiantes
estudiantes = []


# Menú principal
def menu():
    print("\n--- Sistema de Gestión para Profesores de Inglés ---")
    print("1. Registrar estudiante")
    print("2. Ingresar calificaciones")
    print("3. Ver lista de estudiantes")
    print("4. Salir")


# Registrar estudiante
def registrar_estudiante():
    print("\n--- Registrar Estudiante ---")
    nombre = input("Ingrese el nombre del estudiante: ")
    estudiantes.append({"nombre": nombre, "calificaciones": []})
    print(f"Estudiante {nombre} registrado con éxito.")


# Ingresar calificaciones
def ingresar_calificaciones():
    print("\n--- Ingresar Calificaciones ---")
    for idx, estudiante in enumerate(estudiantes):
        print(f"{idx + 1}. {estudiante['nombre']}")

    opcion = int(input("Seleccione el número del estudiante: ")) - 1
    if 0 <= opcion < len(estudiantes):
        calificacion = float(
            input(f"Ingrese la calificación para {estudiantes[opcion]['nombre']}: ")
        )
        estudiantes[opcion]["calificaciones"].append(calificacion)
        print("Calificación registrada con éxito.")
    else:
        print("Opción inválida.")


# Ver lista de estudiantes
def ver_estudiantes():
    print("\n--- Lista de Estudiantes ---")
    for estudiante in estudiantes:
        promedio = (
            sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"])
            if estudiante["calificaciones"]
            else 0
        )
        print(f"Nombre: {estudiante['nombre']}, Promedio: {promedio:.2f}")


# Bucle principal
while True:
    menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_estudiante()
    elif opcion == "2":
        ingresar_calificaciones()
    elif opcion == "3":
        ver_estudiantes()
    elif opcion == "4":
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
