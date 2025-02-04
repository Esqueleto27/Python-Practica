# xargs
# se puede pasar una cantidad infinita de valores
def suma_valores_infinitos(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(f"El resultado de la suma es: {resultado}")


suma_valores_infinitos(1, 2, 3, 4)
