
def comparar_longitud(palabra1, palabra2):
    """
     Compara las longitudes de 2 palabras.

    PARAMS:
        palabra1 (str): Primera palabra
        palabra2 (str): Segunda palabra
    RETURN:
        bool: True si tienen la misma longitud, False en caso contrario
    """
    longitud1 = len(palabra1)
    longitud2 = len(palabra2)
    
    isEqual = longitud1 == longitud2
    
    return isEqual

result = comparar_longitud("Frontend", "Backend")
print(f"Son Frontend y Backend dos palabras con la misma longitud? {result}")


