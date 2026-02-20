# Simulador de Calculadora de Calorias

def calcular_calorias(carbohidratos,proteinas,grasas):
    """
    Calcular las calorias de una persona
    
    Paramatros:
        Carbohidratos (int): Carbohidratos de una persona
        Proteina (int): Consumo de una persona
        Grasas (int): }
        
    Retorna:
        Total Calorias (int): El total de calorias consumidas
    """
    gramo_carbohidratos = carbohidratos * 4
    gramo_proteinas = proteinas * 4
    gramo_grasas = grasas * 9
    
    calorias_totales = gramo_carbohidratos + gramo_proteinas + gramo_grasas
    
    print("=== RESULTADOS ===")
    print(f"Carbohidratos: {gramo_carbohidratos} calorias ")
    print(f"Proteinas: {gramo_proteinas} calorias ")
    print(f"Grasas: {gramo_grasas} calorias ")

    print(f"Total de calorias: {calorias_totales} kcal")

    return calorias_totales

    
calcular_calorias(10,40,5)
