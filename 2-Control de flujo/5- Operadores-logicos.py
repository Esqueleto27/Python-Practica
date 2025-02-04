# Preguntar al usuario si es estudiante
respuesta_estudiante = input("¿Eres estudiante? (sí/no): ").strip().lower()
es_estudiante = True if respuesta_estudiante == "si" else False  # Convertir a booleano

# Preguntar al usuario si sabe inglés
respuesta_ingles = input("¿Sabes inglés? (sí/no): ").strip().lower()
sabe_ingles = True if respuesta_ingles == "si" else False  # Convertir a booleano

# Usar el operador lógico AND
if es_estudiante and sabe_ingles:
    print("Cumples con ambas condiciones: eres estudiante y sabes inglés.")
else:
    print("No cumples con ambas condiciones.")
