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
df = pd.read_csv("Machine_Learning/ejercicios/datos_estadistica_alumnos.csv")
puntos = df["puntos_prueba"]

# Método 1: bucles
print("***MÉTODO 1***")
cont_puntos = 0

for valor in puntos:
    cont_puntos = cont_puntos + 1

print("Total de valores en la columna puntos:", cont_puntos)

# Método 2: funciones
print("***MÉTODO 2***")
def contar_puntos(puntos):
    cont_puntos = 0

    for valor in puntos:
        cont_puntos = cont_puntos + 1

    return cont_puntos

total_puntos = contar_puntos(puntos)
print("Total de valores en la columna puntos:", total_puntos)

# Método 3: pandas
print("***MÉTODO 3***")
print("Primeras filas:")
print(df.head())
print("Total de valores en la columna puntos:", len(puntos))

# Ejercicio 2. Media
# - Calcula la media de puntos_prueba con el Método 1: bucle for, acumulador y len().
# - Calcula la misma media con el Método 2: sum(), len() y, si quieres practicarlo, map() con lambda.
# - Calcula la misma media con el Método 3: pandas usando .mean().
# - Muestra los tres resultados con nombres claros: media_bucle, media_funciones y media_pandas.
# - Comprueba que los tres resultados coinciden.
# - Explica qué significa esa media en el contexto de la prueba.
# Pandas que puedes usar: df["puntos_prueba"].mean().
print("***Solución del ejercicio 2***")

# Método 1: bucles
print("***MÉTODO 1***")
suma = 0
for valor in puntos:
    suma += valor
media_bucle = suma / len(puntos)
print("Media puntos:", media_bucle)

# Método 2: funciones
print("***MÉTODO 2***")
def calcular_media(puntos):
    # Calcular la media sumando todos los valores y dividiendo
    # el resultado entre la cantidad de elementos
    media = sum(puntos) / len(puntos)

    # Devolver la media calculada
    return media

# Llamar a la función y guardar el resultado
media_funciones = calcular_media(puntos)

# Función lambda que calcula la media
media_funcion_lambda = sum(map(lambda x: x, puntos)) / len(puntos)

# Mostrar el resultado
print("Media puntos:", media_funciones)
print("Media puntos:", media_funcion_lambda)

# Método 3: pandas
print("***MÉTODO 3***")
media_pandas = df["puntos_prueba"].mean() 
print("Media puntos:", media_pandas)

# Ejercicio 3. Mediana
# - Calcula la mediana de puntos_prueba con el Método 1: ordenar la lista, comprobar si la cantidad de datos es par o impar y acceder por índice.
# - Calcula la misma mediana con el Método 2: sorted(), len() y acceso por índice. En este caso map() no es necesario.
# - Calcula la misma mediana con el Método 3: pandas usando .median().
# - Muestra los tres resultados con nombres claros: mediana_bucle, mediana_funciones y mediana_pandas.
# - Comprueba que los tres resultados coinciden.
# - Explica por qué la mediana representa el centro de los datos.
# Pandas que puedes usar: df["puntos_prueba"].median().
print("***Solución del ejercicio 3***")

# Método 1: bucles
print("***MÉTODO 1***")
lista_puntos = []
cont_puntos = 0
posicion = 0
punto_anterior = 0
punto_central = 0
mediana_bucle = 0

# Guardar los puntos en una lista y contarlos
for punto in puntos:
    lista_puntos.append(punto)
    cont_puntos = cont_puntos + 1

# Ordenar lista
# Uso de dos bucles para comparar el un elemento con todos los de después
for i in range(len(lista_puntos)):
    for j in range(i+1, len(lista_puntos)):
        if lista_puntos[i] > lista_puntos[j]:
            aux = lista_puntos[i]
            # variable aux guarda un valor de forma temporal
            lista_puntos[i] = lista_puntos[j]
            lista_puntos[j] = aux
            
# Buscar los valores centrales
for punto in lista_puntos:
    if posicion == (cont_puntos//2) - 1:
        punto_anterior = punto
    if posicion == cont_puntos//2:
        punto_central = punto
    posicion += 1

# Si el número de puntos es par
if cont_puntos % 2 == 0:
    mediana_bucle = (punto_anterior + punto_central)/2
    print("Mediana:",mediana_bucle)

# Si el número de puntos es impar
else:
    for punto in lista_puntos:
        cont_puntos = cont_puntos + 1
    for punto in lista_puntos:
        if posicion == (cont_puntos//2):
            mediana_bucle = punto
            print("Mediana:",mediana_bucle)
        posicion += 1

# Método 2: funciones
print("***MÉTODO 2***")

def calcular_mediana(puntos):

    lista_puntos = []
    lista_puntos_ordenada = []
    total_puntos = 0
    posicion = 0
    punto_anterior = 0
    punto_central = 0
    mediana = 0

    # Guardar los puntos en una lista y contarlos
    for punto in puntos:
        lista_puntos.append(punto)
        lista_puntos_ordenada = sorted(lista_puntos)
        total_puntos = len(lista_puntos_ordenada)

    # Buscar los valores centrales
    for punto in lista_puntos_ordenada:
        if posicion == (total_puntos // 2) - 1:
            punto_anterior = punto

        if posicion == total_puntos // 2:
            punto_central = punto

        posicion += 1

    # Si el número de puntos es par
    if total_puntos % 2 == 0:
        mediana = (punto_anterior + punto_central) / 2

    # Si el número de puntos es impar
    else:
        posicion = 0

        for punto in lista_puntos_ordenada:
            if posicion == total_puntos // 2:
                mediana = punto

            posicion += 1

    return mediana

# Llamar a la función
mediana_funciones = calcular_mediana(puntos)
print("Mediana:", mediana_funciones)


# Método 3: pandas
print("***MÉTODO 3***")
mediana_pandas = puntos.median()
print("Mediana:",mediana_pandas)

# Ejercicio 4. Moda
# - Calcula la moda de puntos_prueba con el Método 1: recorre la lista con un bucle y crea un diccionario de frecuencias. 
# - Calcula la misma moda con el Método 2: usa set(), count(), max() y una lambda para encontrar el valor más repetido.
# - Calcula la misma moda con el Método 3: pandas usando .mode().
# - Muestra los tres resultados con nombres claros: moda_bucle, moda_funciones y moda_pandas.
# - Comprueba que los tres resultados coinciden.
# - Explica qué significa que ese valor sea la moda.
# Pandas que puedes usar: df["puntos_prueba"].mode().
print("***Solución del ejercicio 4***")

# Método 1: bucles
print("***MÉTODO 1***")
cont_iguales = 1
cant_mayor = 0
moda_bucle = 0
frecuencias = {}
for i in range (len(lista_puntos)):
    # Procesar cada valor distinto una sola vez
    if lista_puntos[i] not in frecuencias:
        # Reiniciar contador 
        cont_iguales = 1
    
        for j in range(i+1, len(lista_puntos)):
            if lista_puntos[i] == lista_puntos[j]:
                cont_iguales = cont_iguales + 1

        # Guardar la frecuencia del elemento
        frecuencias[lista_puntos[i]] = cont_iguales

        # Variable cant_mayor almacena la cantidad más alta de repeticiones.
        # Comparar cantidad de veces que aparece cada elemento con valor de cant_mayor
        if cont_iguales > cant_mayor:
            cant_mayor = cont_iguales
            moda_bucle = lista_puntos[i]

print("Diccionario de frecuencias:", frecuencias)
print("Moda:", moda_bucle)

# Método 2: funciones
print("***MÉTODO 2***")
def calcular_moda(lista_puntos):
    # Crear un conjunto con los valores únicos de la lista,
    valores_unicos = set(lista_puntos)

    # Buscar el valor que aparece más veces en la lista.
    # lambda x cuenta cuántas veces aparece cada valor (x).
    # max() devuelve el valor cuya frecuencia es más alta.
    moda_funciones = max(
        valores_unicos,
        key=lambda x: lista_puntos.count(x)
    )

    # Devolver el valor que tiene la frecuencia más alta.
    return moda_funciones


moda_funciones = calcular_moda(lista_puntos)

print("Moda:", moda_funciones)

# Método 3: pandas
print("***MÉTODO 3***")
moda_pandas = puntos.mode()
print("Moda:", moda_pandas)

# Ejercicio 5. Desviación de cada dato respecto a la media
# - Calcula primero la media de puntos_prueba.
# - Calcula una lista de desviaciones con el Método 1: bucle for y append(). Cada valor debe ser punto - media.
# - Calcula la misma lista con el Método 2: map() y lambda.
# - Calcula las mismas desviaciones con el Método 3: pandas, restando la media directamente a la columna y creando una columna llamada desviacion.
# - Muestra las tres versiones y comprueba que contienen los mismos valores.
# - Explica qué significa que una desviación sea positiva, negativa o cero.
# Pandas que puedes usar: df["desviacion"] = df["puntos_prueba"] - media.
print("***Solución del ejercicio 5***")

# Método 1: bucles
print("***MÉTODO 1***")
suma = 0
calculo_desviacion = 0
lista_desviacion = []
for valor in puntos:
    suma += valor
media_bucle = suma / len(puntos)
for punto in puntos:
    calculo_desviacion = punto - media_bucle
    lista_desviacion.append(calculo_desviacion)
print(lista_desviacion)

# Método 2: funciones
print("***MÉTODO 2***")
def calcular_desviaciones(puntos):
    # Calcular la media utilizando la expresión anterior
    media_funciones = sum(map(lambda x: x, puntos)) / len(puntos)

    # Calcular la desviación de cada punto respecto a la media
    for punto in puntos:
        calculo_desviacion = punto - media_funciones

        # Mostrar la desviación calculada
        print(calculo_desviacion)

# Llamar a la función
calcular_desviaciones(puntos)

# Método 3: pandas
print("***MÉTODO 3***")
desviacion = df["desviacion"] = df["puntos_prueba"] - media_pandas
print("Desviación:", desviacion)

# Ejercicio 6. Varianza
# - Calcula la varianza de puntos_prueba con el Método 1: bucle for, desviaciones, cuadrados y promedio final.
# - Recuerda: primero se calcula cada desviación, después se eleva al cuadrado y finalmente se hace la media de esos cuadrados.
# - Calcula la misma varianza con el Método 2: map(), lambda, sum() y len().
# - Calcula la misma varianza con el Método 3: pandas usando ddof=0.
# - Muestra los tres resultados con nombres claros: varianza_bucle, varianza_funciones y varianza_pandas.
# - Comprueba que los tres resultados coinciden.
# - Explica qué nos dice la varianza sobre el grupo.
# Pandas que puedes usar: df["puntos_prueba"].var(ddof=0).
print("***Solución del ejercicio 6***")

# Método 1: bucles
print("***MÉTODO 1***")
suma = 0
suma_desviacion = 0
cont_desviacion = 0
for valor in puntos:
    suma += valor
media_bucle = suma / len(puntos)
for punto in puntos:
    desviacion = punto - media_bucle
    desviacion_elevada = desviacion * desviacion
    suma_desviacion += desviacion_elevada
    cont_desviacion = cont_desviacion + 1
    varianza_bucle = suma_desviacion / cont_desviacion
print("Varianza:", varianza_bucle)

# Método 2: funciones
print("***MÉTODO 2***")
def calcular_varianza(puntos):
    # Calcular la media utilizando la expresión anterior
    media_funciones = sum(map(lambda x: x, puntos)) / len(puntos)

    

# Método 3: pandas
print("***MÉTODO 3***")
varianza_pandas = df["puntos_prueba"].var(ddof=0)
print("Varianza:", varianza_pandas)