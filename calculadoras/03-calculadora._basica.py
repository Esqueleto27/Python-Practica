print("***Bienvenidos a la calculadora de Matheo***")
print("Para elejir su operacion debe escribir suma, resta, multiplicacion, division")

n1 = int(input("Ingrese su primer numero:  "))

operacion = input(
    "Escriba \"suma\"  \"resta\"  \"multiplicacion\"  \"division\"").strip().lower()

n2 = int(input("Ingrese su segundo numero:  "))

if operacion == "suma":
    resultado = n1+n2
elif operacion == "resta":
    resultado = n1-n2
elif operacion == "division":
    resultado = n1/n2
elif operacion == "multiplicacion":
    resultado = n1*n2
else:
    resultado = "Algo esta mal..."

print(resultado)
