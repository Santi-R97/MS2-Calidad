def calcular_total(precio, descuento):
    if descuento < 0 or descuento > 100:
        raise ValueError("El descuento debe estar entre 0 y 100")

    return precio - (precio * descuento / 100)
