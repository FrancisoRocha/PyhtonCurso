

def cabecera():
    """Muestra la cabecera de la Aplicacion"""
    title = r"""
   ______                              ______                   
  / ____/____ _ ____ ___   ___   _____/_  __/____ _ ____ _ _____
 / / __ / __ `// __ `__ \ / _ \ / ___/ / /  / __ `// __ `// ___/
/ /_/ // /_/ // / / / / //  __// /    / /  / /_/ // /_/ /(__  ) 
\____/ \__,_//_/ /_/ /_/ \___//_/    /_/   \__,_/ \__, //____/  
                                                 /____/          
            🎮 ¡Crea tu identidad gamer! 🎮
"""
    print(title)


def crear_tag_basico(nombre):
    """
    Crea un gamertag basico usando las primeras 4 letras
    
    Parametro: 
    nombre (str): Nombre del usuario
    
    Retorna:
    str : GamerTag basico
    """
    tag = nombre[:4]
    return tag

def crear_tag_invertido(nombre):
    """
    Crear un gamertag invirtiendo el nombre completo
    
    Parametro:
    nombre (str): El nombre del usuario
    
    Retorna:
    str: Nombre invertido
    """
    tag = nombre[::-1]
    return tag

def crear_tag_intercalado(nombre,apellido):
    """
    Crear un gamertag intercalando el nombre completo
    
    Parametro:
    nombre (str): El nombre del usuario
    apellido (str): El apellido del usuario
    
    Retorna:
    str: Nombre intercalado
    str: Apellido intercalado
    """
    primera_letra = nombre[0]
    segunda_letra = apellido[0]
    resto_nombre = nombre[1:]
    resto_apellido = apellido[1:]
    print("3. TAG INTERCALADO: ", primera_letra, segunda_letra, resto_nombre, resto_apellido, sep="")

def crear_tag_elite(nombre):
    """
    Crea un gamertag "elite" usando inicio y final del nombre.
    Ejemplo: "Santiago" → "Sago"
    
    Parámetro:
    nombre (str): El nombre del usuario
    
    Retorna:
    None (imprime directamente)
    """
    #? Codigo que yo realice
    # primerasdos_letra = nombre[:2]
    # ultimassdos_letra = nombre[-2:]
    # tag = primerasdos_letra, ultimassdos_letra
    print("4. TAG ELITE: ", nombre[:2] , nombre[-2:] ,sep="")
    
def crear_tag_con_numero(nombre, number_favorito):
    """
    Crea un gamertag añadiendo número al final.
    
    Parámetros:
    nombre (str): El nombre del usuario
    numero_favorito (int): Número favorito del usuario
    
    Retorna:
    None (imprime directamente)
    """
    #? CODIGO QUE YO REALICE 
    # primeras_letras = nombre[:5]
    # numero_fav = number_favorito
    # tag = primeras_letras,numero_fav
    print("5. TAG CON NUMERO: ", nombre[:5], number_favorito, sep="")

def mostrar_estadisticas(nombre):
    """
    Muestra estadísticas del nombre proporcionado.
    
    Parámetro:
    nombre (str): El nombre a analizar
    
    Retorna:
    None (imprime directamente)
    """
    nombre_completo = nombre
    longitud_nombre = len(nombre)
    primera_letra = nombre[0]
    ultima_letra = nombre[-1]
    
    print("\n=============================")
    print("📊 ESTADISTICAS DE TU NOMBRE:")
    print("==============================")
    print("Nombre Completo:", nombre_completo)
    print("Longitud del nombre:", longitud_nombre)
    print("Primera Letra:", primera_letra)
    print("Ultima Letra:", ultima_letra)

def monstrar_todas_opciones(nombre, apellido, numero):
    """
    Genera y muestra todas las opciones de gamertags
    
    Parametros:
    nombre (str): Nombre del usuario
    apellido (str): Apellido del usuario
    numero (int): Numero favorito
    
    Retorna:
    None (Imprime Directamente)
    """
    print("\n=============================")
    print("🎯 TUS OPCIONES DE GAMERTAG: ")
    print("==============================")
    
    tag_basico = crear_tag_basico(nombre)
    tag_invertido = crear_tag_invertido(nombre)
    tag_basico = crear_tag_basico(nombre)
    
    print("\n1. TAG BASICO:", tag_basico)
    print("2. TAG INVERTIDO:", tag_invertido)
    crear_tag_intercalado(nombre, apellido)
    crear_tag_elite(nombre)
    crear_tag_con_numero(nombre,numero)
    
    print("\n==============================")


# ===========================================
# Aplicacion Principal
# ===========================================

# Mostrar cabecera
cabecera()

# Solicitar Datos al usuario 
nombre = input("\n👤 Introduce tu nombre: ")    
apellido = input("👤 Introduce tu apellido: ")    
numero = input("📱 Introduce tu numero: ")

# Mostrar estadisticas
mostrar_estadisticas(nombre)   

# Generar y mostrar todas las opciones de gamertog
monstrar_todas_opciones(nombre,apellido,numero)

print("\n🌟¡Elige tu favorito y conquista el mundo gamer! 🌟")


