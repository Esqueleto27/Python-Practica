# Verificacion de estudiante para ir al work and travel

print("")
print("   Verificacion de aplicante para el work and travel  ")

# Verficacion de edad
edad = int(input("Ingrese su edad al dia de hoy: "))
if 17 < edad < 28:
    edad = True
else:
    edad = False

# Verificacion de estudiante

estudiante = input("Es estudiante a tiempo completo? (SI/NO): ").lower().strip()
if estudiante == "si":
    estudiante = True
elif estudiante == "no":
    estudiante = False
else:
    print("Pongase en contacto con uno de nuestros agentes")

# Cantidad de semestres
cantidad_semestres = int(input("Cuantos semestres tiene su carrera?: "))

# Semestre actual
semestre_actual = int(input("Ingrese en que semestre se encuentra actualmente?: "))

# Verificacion semestre
semestre = False if cantidad_semestres == semestre_actual else True


# Resultado
if edad and estudiante and semestre:
    print("Si puede participar")
else:
    print("No puede participar")
