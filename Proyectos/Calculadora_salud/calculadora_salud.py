# =============================
# CALCULADORA DE FITNESS Y SALUD PERSONAL
# =============================


def calcular_imc(peso_kg, altura_m):
    """
    Calcula el indice de Masa Corporal (IMC).

    Formula: IMC = peso / (altura^2)

    Parametros:
    peso_kg (float) --> Peso en kilogramos
    altura_m (float) -->  Altura  en metros

    Retorna:
    float: El IMC Calculado
    """
    imc = peso_kg / (altura_m**2)
    return imc


def es_peso_saludable(imc):
    """
    Determinar si el IMC esta en rango saludable (18.5 - 24.9)

    Parametro:
    imc (float) --> Indice de Masa Corporal

    Retorna:
    bool --> True si esta en rango saludable, False si no esta
    """
    # Operadores de comparacion y logicos
    return imc >= 18.5 and imc <= 24.9


def tiene_sobrepeso(imc):
    """
    Determinar si una persona tiene sobrepeso ( <= 25 )
    """
    return imc >= 25


def tiene_bajo_peso(imc):
    """
    Descripción: Determina si una persona tiene bajo peso según su IMC.
    """
    return imc <= 18.5


def calcular_calorias_diarias(peso_kg, altura_cm, edad, es_hombre):
    """
    Calcula las calorías diarias recomendadas usando Fórmula de Harris-Benedict.

    Parámetros:
    peso_kg (float): Peso en kg
    altura_cm (float): Altura en cm
    edad (int): Edad en años
    es_hombre (bool): True si es hombre, False si es mujer

    Retorna:
    float: Calorías diarias recomendadas
    """
    # Operadores aritméticos y booleanos
    # Fórmula para hombres: 88.362 + (13.397 × peso) + (4.799 × altura) - (5.677 × edad)
    # Fórmula para mujeres: 447.593 + (9.247 × peso) + (3.098 × altura) - (4.330 × edad)
    caloria_hombres = 88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * edad)
    caloria_mujeres = 447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * edad)
    # Usa el hecho de que True = 1 y False = 0
    return es_hombre * caloria_hombres + (1 - es_hombre) * caloria_mujeres


def calcular_agua_diaria(peso_kg):
    """
    Calcula litros de agua recomendados al día (35ml por kg de peso).
    """
    mi_agua = peso_kg * 35
    litros_agua = mi_agua / 1000
    return litros_agua


def calcular_ritmo_cardiaco_maximo(edad):
    """
    Calcula el ritmo cardíaco máximo (220 - edad).
    """
    return 220 - edad


def generar_reporte_completo(nombre, peso, altura, edad, es_hombre):
    """
    Generar un reporte completo de salud y fitness
    """
    print("=" * 60)
    print(f"\n 📊 REPORTE DE FITNESS Y SALUD - {nombre}")
    print("=" * 60)

    # Calculos
    imc = calcular_imc(peso, altura)
    calorias = calcular_calorias_diarias(peso, altura * 100, edad, es_hombre)
    agua = calcular_agua_diaria(peso)
    fc_max = calcular_ritmo_cardiaco_maximo(edad)

    # Informacion Basica
    print("\n👤 Datos Personales")
    print(f"    Peso: {peso} kg")
    print(f"    Altura: {altura} m")
    print(f"    Edad: {edad} años")
    print(f"   ¿Es Hombres?: {es_hombre}")

    # IMC & SALUD
    print("\n💪 Indice de Masa Corporal (IMC)")
    print(f" Tu IMC es: {round(imc, 2)}")
    print(f" ¿Peso Saludable?: {es_peso_saludable(imc)}")
    print(f" ¿Sobrepeso?: {tiene_sobrepeso(imc)}")
    print(f" ¿Bajo Peso?: {tiene_bajo_peso(imc)}")

    # Calorias
    print("\n🔥 Calorías Diarias")
    print(f" Tu meta de calorías es: {round(calorias, 0)} kcal")

    # Agua
    print("\n💧 Agua Diaria")
    print(f" Tu meta de agua es: {round(agua, 2)} litros")

    # Ritmo Cardiaco Maximo
    print("\n❤️‍🩹 Zona Cardiaca")
    print(f" Tu ritmo cardíaco máximo es: {fc_max} bpm")
    print(
        f" Zona cardiaca optima: {round(fc_max * 0.6, 0)} - {round(fc_max * 0.8, 0)} bpm"
    )

    print("\n" + "=" * 60)


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

cabecera = """
╔════════════════════════════════════════════════════════════╗
║     💪 CALCULADORA DE FITNESS Y SALUD PERSONAL 💪          ║
║                                                            ║
║        ¡Descubre tus métricas de salud óptimas!            ║
╚════════════════════════════════════════════════════════════╝
"""
print(cabecera)

# Solicitar datos al usuario
nombre = input("\n👤 ¿Cual es tu nombre?: ")
peso = float(input("⚖️ ¿Cuanto pesas (kg)?: "))
altura = float(input("📏 ¿Cuanto mides (metros, ej. 1.75)? "))
edad = int(input("📅 ¿Cuanto años tienes?: "))
sexo = input("♂️♀️ ¿Cuál es tu sexo (H/M)?: ")

# Convertir sexo a booleano
es_hombre = sexo == "h" or sexo == "H" or sexo == "Hombre" or sexo == "hombre"

# Generado el reporte
generar_reporte_completo(nombre, peso, altura, edad, es_hombre)

print("\n❤️‍🩹 Cuida tu salud, mantén un estilo de vida saludable.")
