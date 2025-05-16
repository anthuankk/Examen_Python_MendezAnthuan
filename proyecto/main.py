from calculos import calcular_propina, calcular_total_con_propina, dividir_total
from utils import obtener_float, obtener_int

def calcular_propina_total():
    print("\n=============================================")
    print("  Cálculo de Propina")
    print("=============================================")
    total = obtener_float("Ingrese el monto total de la cuenta: $")
    porcentaje = obtener_float("Ingrese el porcentaje de propina (por ejemplo: 15): ")
    propina = calcular_propina(total, porcentaje)
    total_con_propina = calcular_total_con_propina(total, propina)
    print("=============================================")
    print(f"La propina calculada es: ${propina:.2f}")
    print(f"El total a pagar es: ${total_con_propina:.2f}")
    print("=============================================")

def dividir_cuenta():
    print("\n=============================================")
    print("  Dividir Cuenta entre Varias Personas")
    print("=============================================")
    total = obtener_float("Ingrese el monto total de la cuenta: $")
    porcentaje = obtener_float("Ingrese el porcentaje de propina (por ejemplo: 15): ")
    personas = obtener_int("Ingrese el número de personas: ")
    propina = calcular_propina(total, porcentaje)
    total_con_propina = calcular_total_con_propina(total, propina)
    total_por_persona = dividir_total(total_con_propina, personas)
    print("=============================================")
    print(f"La propina calculada es: ${propina:.2f}")
    print(f"El total a pagar es: ${total_con_propina:.2f}")
    print(f"Monto por persona: ${total_por_persona:.2f}")
    print("=============================================")

def main():
    while True:
        print("\n=============================================")
        print("  SIMULADOR DE PROPINA")
        print("=============================================")
        print("1. Calcular propina y total a pagar")
        print("2. Calcular total a pagar divido entre varias personas")
        print("3. Salir")
        print("=============================================")
        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "1":
            while True:
                calcular_propina_total()
                repetir = input("¿Deseas calcular nuevamente? (Si/No): ").strip().lower()
                if repetir != 's':
                    break
        elif opcion == "2":
            while True:
                dividir_cuenta()
                repetir = input("¿Deseas calcular nuevamente? (Si/No): ").strip().lower()
                if repetir != 's':
                    break
        elif opcion == "3":
            print("=============================================")
            print("¡Gracias por usar el Simulador de Propina!")
            print("=============================================")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
