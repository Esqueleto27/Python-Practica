# Ejercicio largo con condiciones de if,else,elif
print("***** Bienvenido a nuestro sistema de recompensas por edad ***** ")
nombre_usuario = input("Ingrese su nombre: ")

edad = int(input("Ingrese su edad:"))
if edad > 65:
    print(f"{nombre_usuario} tiene %50 de descuento")
elif edad > 18:
    print(f"{nombre_usuario} tiene que pagar la tarifa base")
elif edad > 6:
    print(f"{nombre_usuario} tiene %50 de descuento")
elif edad > 0:
    print(f"{nombre_usuario}Puede ingrsar gratis ")
