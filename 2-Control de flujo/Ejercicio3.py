# Formatear nombres

primer_nombre = input("Ingrese su primer nombre: ").capitalize().strip()
segundo_nombre = input("Ingrese su segundo nombre: ").capitalize().strip()
primer_apellido = input("Ingrese su primer apellido: ").capitalize().strip()
segundo_apellido = input("Ingrese su segundo apellido: ").capitalize().strip()

nombre_completo = f"{primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido}"
print(nombre_completo)
