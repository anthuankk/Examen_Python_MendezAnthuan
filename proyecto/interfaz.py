def mostrar_menu_propina():
    print("\nSeleccione el porcentaje de propina:")
    print("1. 10%")
    print("2. 15%")
    print("3. 20%")
    print("4. Personalizado")

def mostrar_resultados(propina, total, total_persona=None):
    print("\n--- Resultados ---")
    print(f"Propina: ${propina:.2f}")
    print(f"Total a pagar (con propina): ${total:.2f}")
    if total_persona is not None:
        print(f"Monto por persona: ${total_persona:.2f}")