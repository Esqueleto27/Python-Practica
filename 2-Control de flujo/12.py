while True:
    comando = input("$")
    print(comando)
    if comando.lower() == "salir":  # Salir solo si el comando es "salir"
        break
