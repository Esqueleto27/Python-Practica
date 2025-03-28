from funciones.operadores import suma, resta, multiplicacion, division
from funciones.expresiones import saludo, despedida
from funciones.menu import menu

while True:
    saludo()
    try:
        num1 = int(input("Ingrese su primer número: "))
        num2 = int(input("Ingrese su segundo número: "))
    except ValueError:
        print("❌ Error: Ingrese un número válido. Recuerde que solo pueden ser números enteros.")
        continue

    menu()
    operador = input("Ingrese qué operación desea realizar: ")

    if operador == "5":
        despedida()
        break

    if operador not in ["1", "2", "3", "4"]:
        print("❌ Opción inválida. Intente de nuevo.")
        continue

    if operador == "1":
        print(f" La suma entre {num1} y {num2} es: {suma(num1, num2)}")
    elif operador == "2":
        print(f"➖ La resta entre {num1} y {num2} es: {resta(num1, num2)}")
    elif operador == "3":
        print(f"✖ La multiplicación entre {num1} y {num2} es: {multiplicacion(num1, num2)}")
    elif operador == "4":
        if num2 == 0:
            print("❌ Error: No se puede dividir entre 0.")
        else:
            print(f"➗ La división entre {num1} y {num2} es: {division(num1, num2)}")
