def obtener_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

def obtener_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("Debe ser un número entero positivo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")