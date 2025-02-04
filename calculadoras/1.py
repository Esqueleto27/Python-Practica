# Calculadora completa

print("*****  Bienvenidos a la calculadora de Matheo  *****")
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

operacion = (
    input("Quieres (sumar), (restar), (multiplicar), (dividir): ").lower().strip()
)
if operacion == "suma" or "sumar" or "+":
    resultado = n1 + n2
elif operacion == "resta" or "restar" or "-":
    resultado = n1 - n2
elif operacion == "multiplicacion" or "multiplicar" or "*":
    resultado = n1 * n2
elif operacion == "division" or "dividir" or "/":
    resultado = n1 / n2
else:
    print("Operacion no valida")
print(f"El resultado de {n1} {operacion} {n2} es: {resultado}")
