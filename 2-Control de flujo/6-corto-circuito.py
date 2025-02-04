# entrada a un concierto
gasolina = True
electricidad = True
edad_conductor = int(input("Cuantos años tienes: "))
edad = True if edad_conductor >= 18 else False

if gasolina and electricidad and edad:
    print("Pude manejar")
else:
    print("No puede entrar")
