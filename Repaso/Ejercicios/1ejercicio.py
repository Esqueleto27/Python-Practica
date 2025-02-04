# Contador de vocales
frase = input("Ingrese su frase: ")
vocal = "aeiou"
contador = 0

for letra in frase:
    if letra in vocal:
        contador += 1

print(f'La frase "{frase}" contiene {contador} de vocales ')
