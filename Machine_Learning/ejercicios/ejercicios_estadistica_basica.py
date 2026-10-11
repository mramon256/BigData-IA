import pandas as pd
# Hacer ejercicios de estadística 3 veces
# - Programación y bucles
# - Con funciones y funciones
# - Con pandas

# Ejercicio 1. Carga y exploración de datos
# - Carga el archivo CSV en un DataFrame llamado df.
# - Muestra las primeras filas.
# - Guarda la columna puntos_prueba en una variable llamada puntos.
# - Muestra cuántos datos hay en la columna.
# - Explica con tus palabras qué representa cada fila del CSV.
# Pandas que puedes usar: read_csv(), head(), len().

print("***Solución del ejercicio 1***")
df = pd.read_csv("datos_estadistica_alumnos.csv")

print("***MÉTODE 1***")
