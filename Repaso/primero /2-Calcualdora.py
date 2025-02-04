#Calculadora 
n1=int(input("Ingrese su primer valor: "))
n2=int(input("Ingrese su segundo valor: "))

suma = n1 + n2 
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

resultado = f"""
El resultado de la suma fue: {suma}
El resultado de la resta fue: {resta}
El resultado de la multiplicacion fue: {multiplicacion}
El resultado de la division fue: {division}
"""
print(resultado)
