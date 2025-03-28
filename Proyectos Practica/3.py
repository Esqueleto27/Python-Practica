#Vamos a practiar las variables 
#Ejercicio que que diga los resultados de un estudinate 

nombre = input("Ingrese el nombre del estudinate: ")
grado = int(input("Ingrese el curso del estudiante: "))
calificacion = int(input("Ingrese la calificacion del estudiante: "))

print(f"El estudiante: {nombre} del curso: {grado} tiene la calificacion de: {calificacion}")
if calificacion > 6:
    print(f"El estudiante: {nombre} del curso: {grado} con la calificacion de: {calificacion}, SI PASO")
else:
    print(f"El estudiante: {nombre} del curso: {grado} tiene la calificacion de: {calificacion}, NO PASO ")
