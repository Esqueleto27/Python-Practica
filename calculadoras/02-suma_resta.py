print("***Bienvenidos a la calculadora de Matheo***")
print("Por el momento solo contamos con la operación de suma y resta")

# Pedir al usuario que elija una operación
operacion = input(
    "Escriba 'suma' para sumar o 'resta' para restar: ").strip().lower()

# Pedir al usuario los dos números
n1 = int(input("Ingrese su primer número: "))
n2 = int(input("Ingrese su segundo número: "))

# Realizar la operación según la elección del usuario
if operacion == "suma":
    resultado = n1 + n2
elif operacion == "resta":
    resultado = n1 - n2
else:
    resultado = "Operación no válida"

# Mostrar el resultado
print("Su resultado es:", resultado)
