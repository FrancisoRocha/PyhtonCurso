# Generador de Mensajes Personalizados

def generar_mensaje(nombre,mensaje="Bienvenido al curso de Python"):
    """Retona un mensaje personalizado

        Ejemplo: Hola Francisco, Bienvenido al curso de Pyhton
    
    """
    return f"Hola {nombre} {mensaje}"

print(generar_mensaje("Francisco"))


