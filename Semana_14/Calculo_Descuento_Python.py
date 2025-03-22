# Calcular el descuento

def calcular_descuento (monto_total, porcentaje_descuento=10):
    """
    Se calcula el monto de descuento dado un monto total y un porcentaje de descuento.

    Parametro:
    monto_total (float): Es el monto de la compra.
    porcentaje_descuento (float): Es el porcentaje de descuento que se a aplica (por defecto 10%).

    Retorna:
    float: Es el monto del decuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)

    return descuento

# Montos de las 2 compras
monto_1 = 350
monto_2 = 400
decuento_personalizado = 30

# Se calcula el primer descuento por defecto

descuento_1= calcular_descuento(monto_1)
monto_final_1 = monto_1 - descuento_1 # Se define correctamente el monto final
print(f"Monto total: ${monto_1:.2f} ; Descuento: ${descuento_1:.2f} ; Monto final: ${monto_final_1:.2f}")

# Se calcula el segundo descuento personalizado

descuento_2 = calcular_descuento(monto_2)
monto_final_2 = monto_2 - descuento_2  # Se define correctamente el monto final
print(f"Monto total: ${monto_2:.2f} ; Descuento: ${descuento_2:.2f} ; Monto final: ${monto_final_2:.2f}")

