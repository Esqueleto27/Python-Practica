# Formateador de nombres

n1 = input("Ingrese su primer nombre: ").capitalize()
n2 = input("Ingrese su segundo nombre: ").capitalize()
ap1 = input("Ingrese su primer apellido: ").capitalize()
ap2 = input("Ingrese su segundo apellido: ").capitalize()

nombre_completo = f" {n1} {n2} {ap1} {ap2}"
print(nombre_completo)

nombre_completo_unido = f" {n1} {n2} {ap1} {ap2}".replace(" ", "")
print(nombre_completo_unido)
