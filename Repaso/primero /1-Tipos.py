#Repaso de todo lo visto hasta ahora en tipos de datos 

#1
#String 
nombre = "Matheo"
#Integer 
edad = 21
#Boolean 
masculino = True 
print(f"Tu nombre es: {nombre} y tu edad es: {edad}")

#2 
#Formato de strings 
nombre_del_juego = "Call of Duty"
descripcion = """
Es un shoter tactico
me gusta mucho el juego
"""
#Ahora vamos a imprimir solo una parte de la descripcion
print("De que trata el juego: ",descripcion[0:21])

#4 Metodos de strings 
#Todo en mayusculas 
print(nombre.upper())
#Todo minisculas
print(nombre.lower())
#Primera en mayuscula
print(nombre.capitalize())

#5 Secuencias Escape 
name= "Tu nombre es: \"Matheo\""
print(name)

#6 Numeros 
n1 = 10
n2 = 15
resultado = n1 + n2
print(resultado)
#

#7 Numeros funciones 
#Para redondear 
print(round(1.7))

