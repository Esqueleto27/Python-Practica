# Aplicar descuento

def operacion_descuento():
    total_cuenta = int(input("Ingrese la cantidad de la cuenta: "))
    porcentaje_descuento = int(
        input("Ingrese la cantidad del descuento del dia: "))
    descuento = total_cuenta * (porcentaje_descuento/100)
    total_pagar = total_cuenta - descuento
    print(f"El total a pagar despues del descuento es: {total_pagar}")


operacion_descuento()
