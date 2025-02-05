# estadisticas.py
def media(datos):
    """Esta función calcula la media aritmétrica de una lista con valores numéricos

    Args:
        datos (Lista): Lista de números

    Returns:
        Float: flotante de la media aritmétrica
    """
    return sum(datos) / len(datos)

def calcular_mediana(datos):
    """_summary_

    Args:
        datos (_type_): _description_

    Returns:
        _type_: _description_
    """
    datos_sorted = sorted(datos)
    n = len(datos)
    mid = n // 2
    if n % 2 == 0:
        return (datos_sorted[mid - 1] + datos_sorted[mid]) / 2.0
    else:
        return datos_sorted[mid]