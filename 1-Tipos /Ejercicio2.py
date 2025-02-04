# Conversor de divisas

moneda_local = int(input("Ingrese su valor en su moneda local: "))

USD = moneda_local * 0.050
EUR = moneda_local * 0.047
GBP = moneda_local * 0.039
JPV = moneda_local * 7.71

print(f"""
    En su moneda es: {moneda_local},
    En dolares es: {USD},
    En euros es: {EUR},
    En libras esterlinas es: {GBP},
    En yen japones es: {JPV}
    """)
