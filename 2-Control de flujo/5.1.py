# Programa que indique si vale o no vale la computadora

# or

teclas = input("Las teclas de su teclado estan prendidas? (si/no): ")
teclas_prendidas = True if teclas == "si" else False

pantalla = input("Su pantalla esta prendida? (si?no): ")
pantalla_prendida = True if pantalla == "si" else False

if teclas_prendidas or pantalla_prendida:
    print("La computadora si da señasles de vida")
else:
    print("La computadora esta muerta")
