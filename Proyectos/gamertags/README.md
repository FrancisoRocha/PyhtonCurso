# 🎮 Generador de GamerTags

## 📝 Descripción

**Generador de GamerTags** es un programa en Python que permite crear apodos únicos y personalizados para videojuegos (gamertags) a partir del nombre del usuario. El programa ofrece múltiples estilos de generación y proporciona estadísticas sobre el nombre ingresado.

---

## ✨ Características

El programa genera **5 estilos diferentes** de gamertags:

1. **Tag Básico**: Utiliza las primeras 4 letras del nombre
2. **Tag Invertido**: Invierte completamente el nombre
3. **Tag Intercalado**: Combina iniciales del nombre y apellido con el resto de cada uno
4. **Tag Elite**: Utiliza las primeras 2 y últimas 2 letras del nombre
5. **Tag con Número**: Combina las primeras 5 letras con un número favorito

Además, incluye una función de **estadísticas** que muestra:
- Nombre completo
- Longitud del nombre
- Primera y última letra

---

## 🎯 Objetivos de Aprendizaje

Este proyecto está diseñado para practicar:

- ✅ Manipulación de strings en Python
- ✅ Uso de slicing (corte de cadenas)
- ✅ Funciones personalizadas con parámetros
- ✅ Función `len()` para contar caracteres
- ✅ F-strings y uso de `print()` con `sep=""`
- ✅ Documentación con docstrings

---

## 🚀 Cómo Usar

### Requisitos
- Python 3.x instalado

### Ejecución

1. Clona o descarga el archivo `gamertags.py`
2. Ejecuta el programa:
```bash
   python gamertags.py
```

### Ejemplo de Uso
```python
# Mostrar cabecera
cabecera()

# Generar diferentes tags
nombre = "Francisco"
apellido = "García"
numero = 99

print("1. TAG BÁSICO:", crear_tag_basico(nombre))
print("2. TAG INVERTIDO:", crear_tag_invertido(nombre))
print("3. TAG INTERCALADO:", end=" ")
crear_tag_intercalado(nombre, apellido)
print("4. TAG ELITE:", end=" ")
crear_tag_elite(nombre)
print("5. TAG CON NÚMERO:", end=" ")
crear_tag_con_numero(nombre, numero)

# Mostrar estadísticas
mostrar_estadisticas(nombre)
```

---

## 📊 Ejemplo de Salida
```
   ______                              ______                   
  / ____/____ _ ____ ___   ___   _____/_  __/____ _ ____ _ _____
 / / __ / __ `// __ `__ \ / _ \ / ___/ / /  / __ `// __ `// ___/
/ /_/ // /_/ // / / / / //  __// /    / /  / /_/ // /_/ /(__  ) 
\____/ \__,_//_/ /_/ /_/ \___//_/    /_/   \__,_/ \__, //____/  
                                                 /____/          
            🎮 ¡Crea tu identidad gamer! 🎮

1. TAG BÁSICO: Fran
2. TAG INVERTIDO: ocsicnarF
3. TAG INTERCALADO: FGranciscoarcía
4. TAG ELITE: Frco
5. TAG CON NÚMERO: Franc99

📊 ESTADÍSTICAS DE TU NOMBRE:
Nombre completo: Francisco
Longitud del nombre: 9
Primera letra: F
Última letra: o
```

---

## 🛠️ Funciones Disponibles

| Función | Descripción | Parámetros | Retorno |
|---------|-------------|------------|---------|
| `cabecera()` | Muestra el título ASCII del programa | Ninguno | None |
| `crear_tag_basico(nombre)` | Primeras 4 letras | nombre (str) | str |
| `crear_tag_invertido(nombre)` | Nombre al revés | nombre (str) | str |
| `crear_tag_intercalado(nombre, apellido)` | Intercala iniciales y resto | nombre, apellido (str) | None |
| `crear_tag_elite(nombre)` | Primeras 2 + últimas 2 letras | nombre (str) | None |
| `crear_tag_con_numero(nombre, numero)` | Primeras 5 letras + número | nombre (str), numero (int) | None |
| `mostrar_estadisticas(nombre)` | Muestra info del nombre | nombre (str) | None |

---

## 📖 Conceptos de Python Utilizados

### Slicing (Corte de Strings)
```python
nombre = "Santiago"

nombre[:4]   # "Sant" - Primeras 4 letras
nombre[1:]   # "antiago" - Desde la segunda hasta el final
nombre[-2:]  # "go" - Últimas 2 letras
nombre[::-1] # "ogaitnaS" - Invertir string
```

### Función len()
```python
len("Python")  # Retorna: 6
```

### Print con sep
```python
print("Hola", "Mundo", sep="")  # Salida: HolaMundo
```

---

## 🎓 Nivel de Dificultad

**Principiante** - Ideal para quienes están aprendiendo:
- Variables y tipos de datos
- Funciones básicas
- Manipulación de strings

---

## 👨‍💻 Autor

Proyecto educativo para practicar fundamentos de Python.

---

## 📄 Licencia

Este proyecto es de uso educativo libre.

---

## 🔮 Posibles Mejoras Futuras

- [ ] Añadir más estilos de gamertags
- [ ] Validación de entrada de datos
- [ ] Interfaz gráfica (GUI)
- [ ] Guardar gamertags generados en un archivo
- [ ] Verificar disponibilidad del gamertag en plataformas
- [ ] Generar gamertags aleatorios

---

¿Listo para crear tu identidad gamer? 🚀🎮