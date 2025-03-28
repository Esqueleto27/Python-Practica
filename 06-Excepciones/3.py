#ejercicio basico con try 

#Ejercicio de la edad 
try:
    edad = int(input("Ingrese su edad: "))
except Exception as ex: 
    print("Ocurrio un eror, recuerde que tiene que ser un numero entero")
else:
    print("su edad se gaurdo corectamete ")
finally:
    print("Gracias por preferinos ")