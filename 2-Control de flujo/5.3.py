# Union de todas

# Ejemplo carro is vale o no

gasolina = True
electricidad = True
edad_conductor = int(input("Cuantos años tienes: "))
edad = True if edad_conductor >= 18 else False

if (gasolina and electricidad) and edad:
    print("Puede andar")
else:
    print("Puede andar pero es ilegal")
