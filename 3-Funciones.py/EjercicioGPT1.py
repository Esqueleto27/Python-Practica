# return
# Ejemplo: promedio de
def promedio_año():
    promedio1 = float(input("Ingrese su primer promedio: "))
    promedio2 = float(input("Ingrese su segundo promedio: "))
    promedio3 = float(input("Ingrese su tercer promedio: "))

    promedio_general = promedio1 + promedio2 + promedio3
    promedio = promedio_general / 3
    if promedio >= 7:
        print(f"Pasaste con: {promedio}")
    else:
        print(
            f"No paso porque su promedio es menor a 6 y su promedio es: {promedio}")


promedio_año()
