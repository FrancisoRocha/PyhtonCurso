# Práctica tipos de argumentos en una función

## Objetivo
Programa "La Fiesta de Cumpleaños de Python" aplicando los conceptos de argumentos posicionales, de palabra clave y con valores por defecto en Python.

## Instrucciones
1. Crea una función llamada `organizar_fiesta`: Esta función representará la organización de una fiesta de cumpleaños. La función debe tener tres argumentos:
   * `invitados` (argumento posicional): Un número entero que indica cuántos invitados asistirán.
   * `tema` (argumento de palabra clave con valor por defecto): Una cadena de texto que representa el tema de la fiesta. El valor por defecto debe ser `"Python"`.
   * `lugar` (argumento de palabra clave con valor por defecto): Una cadena de texto que indica dónde se celebrará la fiesta. El valor por defecto debe ser `"aula de informática"`.
2. Dentro de la función `organizar_fiesta`:
   * Imprime un mensaje que diga: `"Preparando una fiesta para [invitados] invitados."`
   * Imprime otro mensaje que diga: `"Tema de la fiesta: [tema]"`
   * Finalmente, imprime: `"Lugar de la celebración: [lugar]"`
3. Prueba la función con diferentes argumentos:
   * Llama a la función proporcionando solo el número de invitados.
   * Llama a la función proporcionando solo el número de invitados y el tema de la fiesta.
   * Llama a la función proporcionando todos los argumentos.

## Resultado esperado
```
Preparando una fiesta para 10 invitados.
Tema de la fiesta: Python
Lugar de la celebración: aula de informática
```