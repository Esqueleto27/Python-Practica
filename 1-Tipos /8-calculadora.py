#
print("***Bienvenidos a la calculadora de Matheo***")

n1 = input("Ingrese su primer numero: ")
n1 = int(n1)

n2 = int(input("Ingrese su segundo numero: "))

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

resultado = f"""
La suma es: {suma},
la resta es: {resta},
la multiplicacion es: {multiplicacion},
la division es: {division}"""

print(resultado)
