# return

def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta


resultado_suma, resultado_resta = operaciones(10, 4)
print(f"Suma: {resultado_suma}, Resta: {resultado_resta}")
