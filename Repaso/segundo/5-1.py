# Operadores logicos
# or basta con que una sea verdadera para que todo sea verdadero

# Ejercicio de si un pasajero puede ingresar al avion teniendo malestares

#
estado_pasajero = input("Se encuentra bien?(SI/NO): ").lower().strip()
if estado_pasajero == "si":
    estado_pasajero = True
else:
    estado_pasajero = False

# Tiene tos
sintoma_tos = input("Ha tenido tos en estos ultimos dias? (SI/NO): ").lower().strip()
if sintoma_tos == "si":
    sintoma_tos = True
else:
    sintoma_tos = False

# Empezamos a trabajar con el operador de or

if estado_pasajero or sintoma_tos:
    print("Puede viajar ")
else:
    print("Usted debe hacerse un examen medico")
