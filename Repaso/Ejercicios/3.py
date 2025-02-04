# Adivina el numero

import random

numero_random = random.randint(1, 100)
adivinado = False

while not adivinado:
    intento = int(input("Ingrese su numero: "))

    if intento < numero_random:
        print("El numero es mayor")
    elif intento > numero_random:
        print("El numero es menor")
    else:
        print(f"correcto!! era el numero :{numero_random}")
        adivinado = True
