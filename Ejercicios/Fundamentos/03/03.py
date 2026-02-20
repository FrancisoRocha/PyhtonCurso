
# PALABRA SECRETA
palabra_adivinar = "python"

def adivinar_palabra(letra_prueba, palabra_intento):
    """
    Determina si una letra está en una palabra específica y si un intento de palabra coincide con esa palabra.
 
    Args:
    letra_prueba (str): La letra a probar si está en la palabra.
    palabra_intento (str): La palabra intentada para adivinar la palabra correcta.
 
    Returns:
    None
    """
    letra_en_palabra = letra_prueba in palabra_adivinar

    print(f"¿ La {letra_prueba} se encuentra en la palabra ? {letra_en_palabra}")

    palabra_igual = palabra_intento == palabra_adivinar
    
    palabra_longitud = len(palabra_intento) == len(palabra_adivinar)
    
    resultado_adivinanza = palabra_igual

    print(f"El jugador gana: {resultado_adivinanza}")
    print(f"Las palabras tiene las misma longitud: {palabra_longitud}")
    
adivinar_palabra("o", "oscar")


