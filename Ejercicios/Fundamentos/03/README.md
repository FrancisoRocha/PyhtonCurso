# Práctica Operadores Identidad, Pertenencia y Lógicos

## Objetivo
Programar un juego de Adivinanza con Letras y Palabras. Este ejercicio tiene como objetivo que practiques con operadores de pertenencia, comparación y operadores lógicos en Python.

## Instrucciones

1. **Palabra a Adivinar:** Al comienzo del programa, define una variable `palabra_adivinar` con un string que será la palabra que los usuarios deben adivinar.

2. **Función `adivinar_palabra`:** Escribe una función llamada `adivinar_palabra`. Esta función debe aceptar dos argumentos: `letra_prueba` y `palabra_intento`.

3. **Verificar Letra en Palabra:**
   - Utiliza operadores de pertenencia para comprobar si `letra_prueba` se encuentra en `palabra_adivinar`.
   - Almacena el resultado (`True` o `False`) en una variable `letra_en_palabra`.
   - Imprime el resultado con el formato: `¿La letra de prueba se encuentra en la palabra? [True/False]`.

4. **Adivinar la Palabra:**
   - Usa operadores de comparación para verificar si `palabra_intento` es igual a `palabra_adivinar`.
   - Combina la operación anterior con operadores lógicos y de comparación para verificar si `palabra_intento` tiene la misma longitud que `palabra_adivinar`.
   - Almacena el resultado en `resultado_adivinanza`.
   - Imprime el resultado con el formato: `El jugador gana: [True/False]`.

5. **Llamar a la Función:**
   - Llama a la función y verifica su correcto funcionamiento proporcionándole como argumento una letra de prueba y una palabra de intento.

## Resultado esperado
¿La letra de prueba se encuentra en la palabra? [True/False]
El jugador gana: [True/False]

## Código
```python
# Palabra a adivinar
palabra_adivinar = "secreto"

def adivinar_palabra(letra_prueba, palabra_intento):
    """
    Determina si una letra está en una palabra específica y si un intento
    de palabra coincide con esa palabra.

    Args:
        letra_prueba (str): La letra a probar si está en la palabra.
        palabra_intento (str): La palabra intentada para adivinar la palabra correcta.

    Returns:
        None
    """
    # Verificar si la letra está en la palabra
    letra_en_palabra = letra_prueba in palabra_adivinar
    print(f"¿La letra de prueba se encuentra en la palabra? {letra_en_palabra}")

    # Verificar si la palabra de intento es igual a la palabra a adivinar y tiene la misma longitud
    resultado_adivinanza = palabra_intento == palabra_adivinar and len(palabra_intento) == len(palabra_adivinar)
    print(f"El jugador gana: {resultado_adivinanza}")

# Ejemplo de uso de la función
adivinar_palabra("p", "python")
```