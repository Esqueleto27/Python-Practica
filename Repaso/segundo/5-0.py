# ejercicio operadores logicos
# and las dos condicioes tienen que ser verdaderas
# Ejmplo irse de work and travel

# Edad
print("Bienvendios a nuestra agencia de work and travel")
edad = int(input("Ingrese su edad: "))
if 17 < edad < 28:
    edad = True
else:
    edad = False

# Estudiante
estudiante = input("Es estudiante? (SI/NO):  ").lower().strip()
if estudiante == "si":
    estudiante = True
elif estudiante == "no":
    estudiante = False
# Numero de semestres totales
numero_semestres = int(input("Cuantos semestres tiene su carrera? : "))

# En que semestre se encuentra actulmente
semestre_actual = int(input("En que semestre se encuentra: "))

# Comparacion de semestres
if numero_semestres == semestre_actual:
    semestre = False
else:
    semestre = True


# Vamos a empezar a trabajar con los operadores logicos

if edad and estudiante and semestre:
    print("Puede aplicar")
else:
    print("No puede aplicar")
