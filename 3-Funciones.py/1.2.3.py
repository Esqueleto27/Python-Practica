# Funciones

def saludo_curso(curso="Sin curso seleccionado todavia"):
    print("**********************************")
    print(f"Bienvenidos al curso de {curso}")
    print("**********************************")


def saludo_estudiante(nombre, apellido):
    print("Gracias por incribirse los nombres del estudiante son:")
    print(f"Tu nombre es: {nombre} y su apellido es: {apellido}")


saludo_curso("python")
saludo_estudiante("Matheo", "Flores")
