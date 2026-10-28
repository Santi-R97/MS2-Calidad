def evaluar_compra(total, es_cliente_premium):
    if total >= 1000:
        if es_cliente_premium:
            return "Descuento premium"
        else:
            return "Descuento general"
    else:
        return "Sin descuento"
