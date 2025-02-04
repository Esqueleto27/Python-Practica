print("***Bienvenidos a la calculadora de Matheo***")
print("Ingrese \"salir\" cuando quiera terminar ")
print("Las operaciones son suma, resta, multiplicacion, division")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese numero: ")
        if resultado.lower().strip() == "salir":
            break

        resultado = int(resultado)

    op = input("Ingrese su operacion: ")
    if op.lower().strip() == "salir":
        break

    n2 = input("Ingrese el otro numero: ")
    if n2.lower().strip() == "salir":
        break

    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multiplicacion":
        resultado *= n2
    elif op.lower() == "division":
        if n2 != 0:  # Evitar la división por cero
            resultado /= n2
        else:
            print("Error: No se puede dividir por cero.")
            break

    print(f"El resultado es: {resultado}")
