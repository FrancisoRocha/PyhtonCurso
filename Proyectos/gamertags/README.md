# Tarea: Generador de GamerTags

## Objetivo
Completar las funciones faltantes de un programa que genera diferentes estilos de gamertags (apodos para videojuegos) a partir del nombre del usuario.

## Instrucciones
Se te proporciona un código parcialmente implementado. Tu tarea es completar las 4 funciones que están vacías siguiendo las indicaciones detalladas más abajo.

## Funciones a completar

### 1. crear_tag_intercalado(nombre, apellido)
**Descripción:** Debe combinar las iniciales del nombre y apellido, seguidas del resto de cada uno.

**Ejemplo:**
- Entrada: nombre="Juan", apellido="Perez"
- Salida esperada: "JPuanerez"

**¿Cómo funciona?**
- Toma la primera letra de "Juan" → "J"
- Toma la primera letra de "Perez" → "P"
- Toma el resto de "Juan" (desde posición 1) → "uan"
- Toma el resto de "Perez" (desde posición 1) → "erez"
- Los junta en ese orden → "JPuanerez"

**Pistas:**
- Usa `nombre[0]` para obtener la primera letra
- Usa `nombre[1:]` para obtener desde la segunda letra hasta el final
- Para mostrar el resultado, usa `print()` con `sep=""` (explicado más abajo)

### 2. crear_tag_elite(nombre)
**Descripción:** Debe tomar las primeras 2 letras y las últimas 2 letras del nombre.

**Ejemplo:**
- Entrada: "Santiago"
- Salida esperada: "Sago"

**¿Cómo funciona?**
- Toma las primeras 2 letras de "Santiago" → "Sa"
- Toma las últimas 2 letras de "Santiago" → "go"
- Las junta → "Sago"

**Pistas:**
- Usa `nombre[:2]` para las primeras 2 letras
- Usa `nombre[-2:]` para las últimas 2 letras (el - cuenta desde el final)

### 3. crear_tag_con_numero(nombre, numero_favorito)
**Descripción:** Debe combinar las primeras 5 letras del nombre con el número favorito.

**Ejemplo:**
- Entrada: nombre="Alexandra", numero_favorito=77
- Salida esperada: "Alexa77"

**Pistas:**
- Usa `nombre[:5]` para obtener las primeras 5 letras
- Puedes poner el número directamente en el `print()`, Python lo mostrará como texto automáticamente

### 4. mostrar_estadisticas(nombre)
**Descripción:** Debe mostrar información estadística sobre el nombre del usuario.

**Debe imprimir:**
```
📊 ESTADÍSTICAS DE TU NOMBRE:
Nombre completo: [nombre]
Longitud del nombre: [cantidad de letras]
Primera letra: [primera letra]
Última letra: [última letra]
```

**Pistas:**
- Usa `len(nombre)` para calcular cuántas letras tiene
- Guarda ese valor en una variable llamada `longitud_nombre`
- Usa `nombre[0]` para la primera letra
- Usa `nombre[-1]` para la última letra
- Haz un `print()` por cada línea que debas mostrar

## Código base
```python
def cabecera():
    """Muestra la cabecera de la aplicación"""
    titulo = r"""
   ______                              ______                   
  / ____/____ _ ____ ___   ___   _____/_  __/____ _ ____ _ _____
 / / __ / __ `// __ `__ \ / _ \ / ___/ / /  / __ `// __ `// ___/
/ /_/ // /_/ // / / / / //  __// /    / /  / /_/ // /_/ /(__  ) 
\____/ \__,_//_/ /_/ /_/ \___//_/    /_/   \__,_/ \__, //____/  
                                                 /____/          
            🎮 ¡Crea tu identidad gamer! 🎮
"""
    print(titulo)
 
def crear_tag_basico(nombre):
    """
    Crea un gamertag básico usando las primeras 4 letras.
 
    Parámetro:
    nombre (str): El nombre del usuario
 
    Retorna:
    str: Gamertag básico
    """
    tag = nombre[:4]
    return tag
 
def crear_tag_invertido(nombre):
    """
    Crear un gamertag invirtiendo el nombre completo.
 
    Parámetro:
    nombre (str): El nombre del usuario
 
    Retorna:
    str: Nombre invertido
    """
    tag = nombre[::-1]
    return tag
 
def crear_tag_intercalado(nombre, apellido):
    """
    Crea un gamertag combinando letras del nombre y apellido.
    Ejemplo: nombre="Juan", apellido="Perez" → "JPuanerez"
    
    Parámetros:
    nombre (str): El nombre del usuario
    apellido (str): El apellido del usuario
    
    Retorna:
    None (imprime directamente)
    """
    # TU CÓDIGO AQUÍ
 
 
def crear_tag_elite(nombre):
    """
    Crea un gamertag "elite" usando inicio y final del nombre.
    Ejemplo: "Santiago" → "Sago"
    
    Parámetro:
    nombre (str): El nombre del usuario
    
    Retorna:
    None (imprime directamente)
    """
    # TU CÓDIGO AQUÍ
 
 
def crear_tag_con_numero(nombre, numero_favorito):
    """
    Crea un gamertag añadiendo número al final.
    
    Parámetros:
    nombre (str): El nombre del usuario
    numero_favorito (int): Número favorito del usuario
    
    Retorna:
    None (imprime directamente)
    """
    # TU CÓDIGO AQUÍ
 
 
def mostrar_estadisticas(nombre):
    """
    Muestra estadísticas del nombre proporcionado.
    
    Parámetro:
    nombre (str): El nombre a analizar
    
    Retorna:
    None (imprime directamente)
    """
    # TU CÓDIGO AQUÍ
```

## Conceptos importantes

### 📌 Slicing (cortar strings)
El slicing te permite obtener partes de un texto usando corchetes `[]`:
```python
nombre = "Santiago"
 
nombre[:4]   # Primeras 4 letras → "Sant"
nombre[1:]   # Desde la segunda letra hasta el final → "antiago"
nombre[-2:]  # Últimas 2 letras → "go"
nombre[0]    # Primera letra → "S"
nombre[-1]   # Última letra → "o"
```

**Importante:** En Python se empieza a contar desde 0, no desde 1.

### 📌 La función len()
Te dice cuántos caracteres tiene un string:
```python
nombre = "Juan"
cantidad = len(nombre)  # Resultado: 4
```

### 📌 Usar print() con sep="" para juntar textos
**¿Qué hace sep?**
- Por defecto, `print()` separa los elementos con un espacio
- Con `sep=""` eliminamos ese espacio y todo queda junto

**Ejemplos:**
```python
# Sin sep (comportamiento normal)
print("Hola", "Mundo")
# Resultado: Hola Mundo (con espacio)
 
# Con sep=""
print("Hola", "Mundo", sep="")
# Resultado: HolaMundo (sin espacio)
 
# Ejemplo con variables
nombre = "Maria"
apellido = "Garcia"
print(nombre[0], apellido[0], nombre[1:], sep="")
# Resultado: MGaria
```

## Consejos
✅ Lee cuidadosamente los docstrings (documentación) de cada función

✅ Observa los ejemplos proporcionados en cada función

✅ Las funciones ya implementadas (`crear_tag_basico` y `crear_tag_invertido`) te dan pistas sobre cómo usar slicing

✅ Recuerda que `len()` te da la longitud de un string

✅ No uses el operador `+`, usa `print()` con múltiples argumentos y `sep=""`

✅ Prueba tu código con diferentes nombres para verificar que funciona

⚠️ La resolución completa se revisará en la próxima clase.

¡Buena suerte! 🚀