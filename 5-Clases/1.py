# El construcutor es una funcion que podemos definir dentro de cada una de nuestras clases y este se va a ejecutar siempre que creemos una instancia
# Se ejecuta cada vez que se crea una nueva instancia de la clase.
# Self es una palabra reservada que se utiliza en todas la clases de python y se usan para referenciar las intancias de las clases


class Perro:
    # Creamos el constructor con __init__
    # Este método inicializa los atributos de la instancia.
    def __init__(self, nombre, edad):
        # `self.nombre` y `self.edad` son propiedades de la instancia.
        self.nombre = (
            nombre  # Propiedad asociada a la instancia para almacenar el nombre.
        )
        self.edad = edad  # Propiedad asociada a la instancia para almacenar la edad.

    # Método de la clase
    def habla(self):
        # Método que imprime un mensaje. Utiliza self para acceder al objeto actual.
        print("Guau")


# Crear instancias de la clase Perro
# Aquí debemos pasar los dos argumentos requeridos por el constructor: nombre y edad.
mi_perro = Perro("Bobi", 3)  # Instancia de la clase Perro con nombre "Bobi" y edad 3.
mi_perro2 = Perro("Max", 5)  # Instancia de la clase Perro con nombre "Max" y edad 5.

# Acceder a los atributos de las instancias
print(mi_perro.nombre)  # Salida: Bobi
print(mi_perro2.nombre)  # Salida: Max

# Llamar al método habla()
mi_perro.habla()  # Salida: Guau
mi_perro2.habla()  # Salida: Guau
