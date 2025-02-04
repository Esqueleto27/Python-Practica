# Sistemas de precios para venta de juegos

juego_uno = "Star Wars con valor de 60"
juego_dos = "Minecraft con valor de 30"
juegos_tres = "Fortnite con un valor de 10"

print(
    f"""
    Tenemos estos juegos disponibles el dia de hoy: 
    {juego_uno},
    {juego_dos},
    {juegos_tres}
"""
)
eleccion_juego = input("Que juego desea? :").lower().strip()
if eleccion_juego == "starwars":
    print("El juego elegido es Star Wars con valor de 60 dolares ")
