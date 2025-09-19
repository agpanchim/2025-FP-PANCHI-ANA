# Programa para calcular el descuento en compras
# Ana Panchi

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento sobre una compra.
    :param monto_total: float, valor total de la compra
    :param porcentaje_descuento: float, porcentaje de descuento (por defecto 10%)
    :return: float, monto del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
if __name__ == "__main__":

    # Llamada 1: usando el porcentaje por defecto
    monto1 = 150.0
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1

    print(f"Compra 1: ${monto1:.2f}")
    print(f"Descuento aplicado (10%): ${descuento1:.2f}")
    print(f"Valor a pagar: ${total1:.2f}\n")

    # Llamada 2: especificando un porcentaje diferente
    monto2 = 200.0
    descuento2 = calcular_descuento(monto2, 15)  # 15% de descuento
    total2 = monto2 - descuento2

    print(f"Compra 2: ${monto2:.2f}")
    print(f"Descuento aplicado (15%): ${descuento2:.2f}")
    print(f"Valor a pagar: ${total2:.2f}")