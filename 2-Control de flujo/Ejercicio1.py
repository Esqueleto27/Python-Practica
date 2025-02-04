# Verificacion de tweets

tweet = input("Ingrese su tweet de maximo 20 caracteres: ")
if not tweet:
    print("No se aceptan caracteres vacios")
elif len(tweet) > 20:
    print("Se ha sobrepasado el limite de caracteres")
else:
    print("Se ha publicado correctamente")
