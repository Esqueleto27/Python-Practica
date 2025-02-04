# Programa para saber si
def resultado(cliente, pago_final):
    cliente = int(input("Cuanto pago: "))
    pago_final = int(input("Cuanto cuesta: "))
    resul = cliente - pago_final
    print(resul)


resultado(12, 12)
