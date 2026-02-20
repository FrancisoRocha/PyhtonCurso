# Practia de Funciones Propias

# Ejercicio 1
def contar_caracteres(textos):
    
    """
        Crear un personalizado y Calcular la longitud
        del texto que introduce el usuario
        
        Args:
            texto (str): Cadena de caracteres a evaluar.
 
        Returns:
            None: La función solo imprime el resultado.
    """
    
    longitud_texto = len(textos)
    print(f"La frase '{textos}' tiene {longitud_texto} caracteres")

contar_caracteres("Aprender Python es divertido")

# Ejercicio 2
def convertir_numero(numeroEntero):
    
    """
        Funcion que imprime el tipo de dato de los numeros
        
        Args:
            numero (int): Número entero a convertir.
 
        Returns:
            None: La función solo imprime el resultado.
    """
    
    entero = numeroEntero
    numeroCadena = str(numeroEntero)
    numeroFloat = float(numeroEntero)
    
    print(f"Entero: {entero}, Tipo: {type(entero)}")
    print(f"Cadena: {numeroCadena}, Tipo: {type(numeroCadena)}")
    print(f"Flotante: {numeroFloat}, Tipo: {type(numeroFloat)}")
    
convertir_numero(50)


