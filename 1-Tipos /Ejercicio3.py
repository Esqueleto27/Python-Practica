# Calculadora de cambio

costo_producto = int(input("Cuanto valio el producto: "))
cantidad_dinero_entregada = int(input("Cuanto dinero entrego el cliente: "))
cambio = cantidad_dinero_entregada - costo_producto
if cantidad_dinero_entregada < costo_producto:
    print("Falta dinero")
else:
    print(f"El cambio es de: {cambio}")
