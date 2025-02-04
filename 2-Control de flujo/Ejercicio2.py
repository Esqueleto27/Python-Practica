# Conversor de divisas

cantidad = int(input("Ingrese la cantidad de dinero a convetir: $"))
divisa = input(
    "En que divisa esta el valor Ejm: 'dolar', 'euro', 'pesos mexicanos': ").lower().strip()


tasa_USD_a_EUR = 0.95
tasa_USD_a_MXN = 20.28
tasa_EUR_A_MXN = 21.36

if divisa == "dolares":
    euro = cantidad * tasa_USD_a_EUR
    pesos = cantidad * tasa_USD_a_MXN
    print(f"{cantidad} dolares son: ")
    print(f"En EUROS es: {euro:.2f}")
    print(f"En PESOS es: {pesos:2f}")
elif divisa == "euros":
    dolar = cantidad / tasa_USD_a_EUR
    pesos = cantidad * tasa_EUR_A_MXN
    print(f"{cantidad} euros son: ")
    print(f"En DOLARES es: {dolar:.2f}")
    print(f"En PESOS es: {pesos:.2f}")
elif divisa == "pesos":
    dolar = cantidad / tasa_USD_a_MXN
    euros = cantidad / tasa_EUR_A_MXN
    print(f"{cantidad} pesos son: ")
    print(f"En DOLARES es: {dolar:.2f}")
    print(f"En EUROS es: {euros:.2f}")
else:
    print("Algo salio mal")
