"""
Diez ejercicios resueltos con bucles, funciones de Python y pandas.

"""

import pandas as pd

def mostrar_resultados(nombre, bucle, funciones, pandas):
    """Muestra los resultados con el nombre de cada método."""
    print(f"{nombre}_bucle = {bucle}")
    print(f"{nombre}_funciones = {funciones}")
    print(f"{nombre}_pandas = {pandas}")


# EJERCICIO 1. Carga y exploración de datos.
print("\nSolución del ejercicio 1")
# Cargamos una sola vez y preparamos los datos para los tres métodos.
df = pd.read_csv("datos_estadistica_alumnos.csv")
puntos = list(df["puntos_prueba"])
filas = df.to_dict("records")

# Método 1: un bucle muestra las filas de las posiciones 0 a 4.
print("Primeras cinco filas con un bucle:")
for i in range(5):
    print(filas[i])

# Método 2: [:5] selecciona las cinco primeras filas de la lista.
print("Primeras cinco filas con funciones de Python:")
print(filas[:5])

# Método 3: head() muestra las cinco primeras filas del DataFrame.
print("Primeras cinco filas con pandas:")
print(df.head())

print("Cantidad de datos:", len(puntos))
print("Cada fila representa un alumno y sus datos de estudio y resultados.")


# EJERCICIO 2. Media.
print("\nSolución del ejercicio 2")

# Método 1: acumulamos las puntuaciones y dividimos entre su cantidad.
suma_bucle = 0
for valor in puntos:
    suma_bucle += valor
media_bucle = suma_bucle / len(puntos)

# Método 2: sum ya realiza la suma; map no es necesario en este cálculo.
media_funciones = sum(puntos) / len(puntos)

# Método 3: mean calcula la media de la columna.
media_pandas = df["puntos_prueba"].mean()

mostrar_resultados("media", media_bucle, media_funciones, media_pandas)
coinciden = media_bucle == media_funciones == media_pandas
print("Coinciden:", coinciden)
print(f"La puntuación media es {media_bucle:g} puntos por alumno.")


# EJERCICIO 3. Mediana.
print("\nSolución del ejercicio 3")

# Método 1: ordenación mediante bucles, conservando la lista original.
# Algoritmo activo: intercambio directo (exchange sort).
# Compara cada posición con todas las posteriores e intercambia al encontrar
# un valor menor. Bubble sort compara e intercambia elementos vecinos.
ordenados_bucle = puntos.copy()
for i in range(len(ordenados_bucle) - 1):
    for j in range(i + 1, len(ordenados_bucle)):
        if ordenados_bucle[j] < ordenados_bucle[i]:
            auxiliar = ordenados_bucle[i]
            ordenados_bucle[i] = ordenados_bucle[j]
            ordenados_bucle[j] = auxiliar

# Alternativa: selection sort (ordenación por selección), sin ejecutar.
# Busca la posición del menor valor de la parte pendiente y después realiza
# el intercambio. No intercambia cada vez que encuentra un valor menor.
# Para probarlo, comenta el bloque anterior y descomenta este.
# ordenados_bucle = puntos.copy()
# for i in range(len(ordenados_bucle) - 1):
#     posicion_minimo = i
#     for j in range(i + 1, len(ordenados_bucle)):
#         if ordenados_bucle[j] < ordenados_bucle[posicion_minimo]:
#             posicion_minimo = j
#     auxiliar = ordenados_bucle[i]
#     ordenados_bucle[i] = ordenados_bucle[posicion_minimo]
#     ordenados_bucle[posicion_minimo] = auxiliar

# Alternativa: bubble sort (ordenación por burbuja), sin ejecutar.
# Compara posiciones vecinas y las intercambia si están en orden incorrecto.
# En cada pasada, el mayor valor de la parte pendiente queda al final.
# Para probarlo, comenta el bloque activo y descomenta este.
# ordenados_bucle = puntos.copy()
# for i in range(len(ordenados_bucle) - 1):
#     for j in range(len(ordenados_bucle) - 1 - i):
#         if ordenados_bucle[j] > ordenados_bucle[j + 1]:
#             auxiliar = ordenados_bucle[j]
#             ordenados_bucle[j] = ordenados_bucle[j + 1]
#             ordenados_bucle[j + 1] = auxiliar

n = len(ordenados_bucle)
if n % 2 == 0:
    mediana_bucle = (ordenados_bucle[n // 2 - 1] + ordenados_bucle[n // 2]) / 2
else:
    mediana_bucle = ordenados_bucle[n // 2]

# Método 2: sorted devuelve una lista ordenada.
ordenados_funciones = sorted(puntos)
n_funciones = len(ordenados_funciones)
if n_funciones % 2 == 0:
    mediana_funciones = (
        ordenados_funciones[n_funciones // 2 - 1]
        + ordenados_funciones[n_funciones // 2]
    ) / 2
else:
    mediana_funciones = ordenados_funciones[n_funciones // 2]

# Método 3: median obtiene el valor central.
mediana_pandas = df["puntos_prueba"].median()

mostrar_resultados("mediana", mediana_bucle, mediana_funciones, mediana_pandas)
coinciden = mediana_bucle == mediana_funciones == mediana_pandas
print("Coinciden:", coinciden)
print("Hay diez datos: se promedian el quinto (70) y el sexto (80).")
print("La mediana es 75: cinco alumnos quedan por debajo y cinco por encima.")


# EJERCICIO 4. Moda. Estos datos tienen una única moda.
# Estas soluciones devuelven una sola moda, aunque haya varias empatadas.
# En caso de empate, los tres métodos podrían elegir valores diferentes.
print("\nSolución del ejercicio 4")

# Método 1: contamos las apariciones en un diccionario.
frecuencias = {}
for valor in puntos:
    if valor in frecuencias:
        frecuencias[valor] += 1
    else:
        frecuencias[valor] = 1

# Si hay empate, conserva la moda que aparece primero en la lista original:
# solo cambia de candidato cuando encuentra una frecuencia mayor, no igual.
moda_bucle = puntos[0]
frecuencia_mayor = 0
for valor in frecuencias:
    if frecuencias[valor] > frecuencia_mayor:
        frecuencia_mayor = frecuencias[valor]
        moda_bucle = valor

# Método 2: set evita repetir candidatos; count mide sus frecuencias.
# En caso de empate, max elige el primer candidato que recorre en el set.
# El set no garantiza el orden original: no tiene por qué ser la primera moda
# que aparecía en la lista de puntos.
moda_funciones = max(set(puntos), key=lambda valor: puntos.count(valor))

# Método 3: mode devuelve una Series; iloc[0] extrae el primer valor.
# mode() obtiene todas las modas ordenadas; iloc[0] conserva solo la primera.
# Con estas puntuaciones numéricas, sería la menor de las modas empatadas.
moda_pandas = df["puntos_prueba"].mode().iloc[0]

mostrar_resultados("moda", moda_bucle, moda_funciones, moda_pandas)
coinciden = moda_bucle == moda_funciones == moda_pandas
print("Coinciden:", coinciden)
print("Frecuencias:", frecuencias)
print(f"La moda es {moda_bucle}: aparece {frecuencia_mayor} veces.")


# EJERCICIO 5. Desviaciones respecto a la media.
print("\nSolución del ejercicio 5")

# Método 1: restamos la media y guardamos cada resultado.
desviaciones_bucle = []
for valor in puntos:
    desviaciones_bucle.append(valor - media_bucle)

# Método 2: map aplica la resta a todos los valores.
desviaciones_funciones = list(map(lambda valor: valor - media_funciones, puntos))

# Método 3: pandas aplica la resta directamente a la columna.
df["desviacion"] = df["puntos_prueba"] - media_pandas
desviaciones_pandas = df["desviacion"].tolist()

mostrar_resultados("desviaciones", desviaciones_bucle, desviaciones_funciones, desviaciones_pandas)
coinciden = desviaciones_bucle == desviaciones_funciones == desviaciones_pandas
print("Coinciden:", coinciden)
print("Negativa: por debajo de la media; positiva: por encima; cero: igual a la media.")


# EJERCICIO 6. Varianza poblacional.
# POBLACIONAL: describe al grupo completo que queremos estudiar (la población).
# Ejemplo: queremos estudiar una clase de diez alumnos y tenemos los datos
# de los diez. Su varianza poblacional se calcula dividiendo entre n, es decir, 10.
#
# MUESTRAL: se refiere a una muestra, una parte de una población mayor.
# Ejemplo: elegimos diez alumnos de un centro con mil y usamos sus datos
# para estimar la variabilidad de los mil. Para esa estimación calculamos
# la varianza muestral dividiendo entre n - 1, es decir, 9.
#
# Aquí estudiamos únicamente a los diez alumnos del CSV y los tratamos como
# la población completa. La elección depende del grupo que queremos estudiar,
# no de que haya muchos o pocos datos.
print("\nSolución del ejercicio 6")

# Método 1: calculamos desviaciones, cuadrados y su promedio.
suma_cuadrados_bucle = 0
for valor in puntos:
    desviacion = valor - media_bucle
    cuadrado = desviacion ** 2
    suma_cuadrados_bucle += cuadrado
varianza_bucle = suma_cuadrados_bucle / len(puntos)

# Método 2: map calcula los cuadrados; sum los acumula.
varianza_funciones = sum(
    map(lambda valor: (valor - media_funciones) ** 2, puntos)
) / len(puntos)

# Método 3: ddof=0 hace que se divida entre n.
# pandas utiliza el divisor n - ddof. Si no lo indicamos, usa ddof=1 y divide
# entre n - 1: es la varianza muestral descrita arriba.
# Indicamos ddof=0 para obtener la poblacional: dividimos entre los diez alumnos.
# En nuestros datos, la suma de cuadrados es 2040: 2040 / 10 = 204.
varianza_pandas = df["puntos_prueba"].var(ddof=0)

mostrar_resultados("varianza", varianza_bucle, varianza_funciones, varianza_pandas)
coinciden = varianza_bucle == varianza_funciones == varianza_pandas
print("Coinciden:", coinciden)
print(f"Suma de cuadrados: {suma_cuadrados_bucle:g}; cantidad de datos: {len(puntos)}.")
print("La varianza es 204 puntos cuadrados y mide la dispersión respecto a la media.")


# EJERCICIO 7. Desviación estándar poblacional.
print("\nSolución del ejercicio 7")

# Método 1: raíz cuadrada de la varianza obtenida con bucles.
desviacion_estandar_bucle = varianza_bucle ** 0.5

# Método 2: media de los cuadrados de las desviaciones y raíz cuadrada.
desviacion_estandar_funciones = (
    sum(map(lambda valor: (valor - media_funciones) ** 2, puntos))
    / len(puntos)
) ** 0.5

# Método 3: std obtiene la raíz cuadrada de la varianza.
# Con ddof=0, esa varianza se calcula dividiendo entre n, como en el ejercicio 6.
# Resultado: raíz cuadrada de 204, aproximadamente 14,28 puntos.
desviacion_estandar_pandas = df["puntos_prueba"].std(ddof=0)

mostrar_resultados(
    "desviacion_estandar",
    desviacion_estandar_bucle,
    desviacion_estandar_funciones,
    desviacion_estandar_pandas,
)
coinciden = (
    desviacion_estandar_bucle == desviacion_estandar_funciones == desviacion_estandar_pandas
)
print("Coinciden:", coinciden)
print("Es aproximadamente 14,28 puntos. Se expresa en puntos, no en puntos cuadrados.")


# EJERCICIO 8. Normalización min-max.
print("\nSolución del ejercicio 8")

# Método 1: buscamos los extremos sin min ni max y normalizamos.
minimo_bucle = puntos[0]
maximo_bucle = puntos[0]
for valor in puntos:
    if valor < minimo_bucle:
        minimo_bucle = valor
    if valor > maximo_bucle:
        maximo_bucle = valor

normalizados_bucle = []
for valor in puntos:
    normalizados_bucle.append((valor - minimo_bucle) / (maximo_bucle - minimo_bucle))

# Alternativa con índices, comentada para que no se ejecute.
# Creamos una posición por cada puntuación, inicialmente con valor 0.
# La asignación por índice sustituye un elemento: no crea posiciones nuevas.
# Si empezáramos con [], la posición 0 no existiría y se produciría un error.
# normalizados_bucle = [0] * len(puntos)
# for i in range(len(puntos)):
#     normalizados_bucle[i] = (
#         (puntos[i] - minimo_bucle) / (maximo_bucle - minimo_bucle)
#     )

# Método 2: extremos con min/max y transformación con map/lambda.
minimo_funciones = min(puntos)
maximo_funciones = max(puntos)
normalizados_funciones = list(map(
    lambda valor: (valor - minimo_funciones) / (maximo_funciones - minimo_funciones),
    puntos,
))

# Método 3: operaciones sobre la columna completa.
minimo_pandas = df["puntos_prueba"].min()
maximo_pandas = df["puntos_prueba"].max()
df["puntos_normalizados"] = (
    (df["puntos_prueba"] - minimo_pandas) / (maximo_pandas - minimo_pandas)
)
normalizados_pandas = df["puntos_normalizados"].tolist()

mostrar_resultados("minimo", minimo_bucle, minimo_funciones, minimo_pandas)
mostrar_resultados("maximo", maximo_bucle, maximo_funciones, maximo_pandas)
mostrar_resultados("normalizados", normalizados_bucle, normalizados_funciones, normalizados_pandas)
coinciden = (
    minimo_bucle == minimo_funciones == minimo_pandas
    and maximo_bucle == maximo_funciones == maximo_pandas
    and normalizados_bucle == normalizados_funciones == normalizados_pandas
)
print("Coinciden:", coinciden)
print("0 corresponde a 50 puntos; 0,5 correspondería a 75 puntos; 1 corresponde a 100 puntos.")


# EJERCICIO 9. Estandarización z-score.
print("\nSolución del ejercicio 9")

# Método 1: reutilizamos la media y la desviación estándar de los bucles.
estandarizados_bucle = []
for valor in puntos:
    estandarizados_bucle.append((valor - media_bucle) / desviacion_estandar_bucle)

# Método 2: map aplica la fórmula a cada puntuación.
estandarizados_funciones = list(map(
    lambda valor: (valor - media_funciones) / desviacion_estandar_funciones,
    puntos,
))

# Método 3: media y desviación estándar de pandas, con ddof=0.
df["puntos_estandarizados"] = (
    (df["puntos_prueba"] - df["puntos_prueba"].mean())
    / df["puntos_prueba"].std(ddof=0)
)
estandarizados_pandas = df["puntos_estandarizados"].tolist()

mostrar_resultados(
    "estandarizados", estandarizados_bucle, estandarizados_funciones, estandarizados_pandas,
)
coinciden = estandarizados_bucle == estandarizados_funciones == estandarizados_pandas
print("Coinciden:", coinciden)
print("Cada z indica cuántas desviaciones estándar separan el dato de la media.")
print("Un z positivo está por encima; uno negativo, por debajo; cerca de cero, cerca de la media.")


# EJERCICIO 10. Interpretación final.
print("\nSolución del ejercicio 10")

# Método 1: filtros y búsqueda de extremos mediante bucles.
encima_bucle = []
debajo_bucle = []
maximo_normalizado_bucle = normalizados_bucle[0]
minimo_normalizado_bucle = normalizados_bucle[0]
distancia_maxima_bucle = abs(desviaciones_bucle[0])
for i in range(len(filas)):
    nombre = filas[i]["nombre"]
    if puntos[i] > media_bucle:
        encima_bucle.append(nombre)
    elif puntos[i] < media_bucle:
        debajo_bucle.append(nombre)
    if normalizados_bucle[i] > maximo_normalizado_bucle:
        maximo_normalizado_bucle = normalizados_bucle[i]
    if normalizados_bucle[i] < minimo_normalizado_bucle:
        minimo_normalizado_bucle = normalizados_bucle[i]
    if abs(desviaciones_bucle[i]) > distancia_maxima_bucle:
        distancia_maxima_bucle = abs(desviaciones_bucle[i])

mayor_normalizado_bucle = []
menor_normalizado_bucle = []
mas_alejados_bucle = []
for i in range(len(filas)):
    if normalizados_bucle[i] == maximo_normalizado_bucle:
        mayor_normalizado_bucle.append(filas[i]["nombre"])
    if normalizados_bucle[i] == minimo_normalizado_bucle:
        menor_normalizado_bucle.append(filas[i]["nombre"])
    if abs(desviaciones_bucle[i]) == distancia_maxima_bucle:
        mas_alejados_bucle.append(filas[i]["nombre"])

# Método 2: filter selecciona las filas y map extrae los nombres.
encima_funciones = list(map(
    lambda fila: fila["nombre"],
    filter(lambda fila: fila["puntos_prueba"] > media_funciones, filas),
))
debajo_funciones = list(map(
    lambda fila: fila["nombre"],
    filter(lambda fila: fila["puntos_prueba"] < media_funciones, filas),
))
mayor_normalizado_funciones = list(map(
    lambda fila: fila["nombre"],
    filter(lambda fila: fila["puntos_prueba"] == maximo_funciones, filas),
))
menor_normalizado_funciones = list(map(
    lambda fila: fila["nombre"],
    filter(lambda fila: fila["puntos_prueba"] == minimo_funciones, filas),
))
# La transformación min-max conserva el orden: los extremos son los mismos.
distancia_maxima_funciones = max(map(lambda valor: abs(valor - media_funciones), puntos))
mas_alejados_funciones = list(map(
    lambda fila: fila["nombre"],
    filter(
        lambda fila: abs(fila["puntos_prueba"] - media_funciones) == distancia_maxima_funciones,
        filas,
    ),
))

# Método 3: condiciones sobre columnas y selección mediante loc.
encima_pandas = df.loc[df["puntos_prueba"] > media_pandas, "nombre"].tolist()
debajo_pandas = df.loc[df["puntos_prueba"] < media_pandas, "nombre"].tolist()
mayor_normalizado_pandas = df.loc[
    df["puntos_normalizados"] == df["puntos_normalizados"].max(), "nombre"
].tolist()
menor_normalizado_pandas = df.loc[
    df["puntos_normalizados"] == df["puntos_normalizados"].min(), "nombre"
].tolist()
distancias_pandas = df["desviacion"].abs()
mas_alejados_pandas = df.loc[distancias_pandas == distancias_pandas.max(), "nombre"].tolist()

mostrar_resultados("encima", encima_bucle, encima_funciones, encima_pandas)
mostrar_resultados("debajo", debajo_bucle, debajo_funciones, debajo_pandas)
mostrar_resultados("mayor_normalizado", mayor_normalizado_bucle, mayor_normalizado_funciones, mayor_normalizado_pandas)
mostrar_resultados("menor_normalizado", menor_normalizado_bucle, menor_normalizado_funciones, menor_normalizado_pandas)
mostrar_resultados("mas_alejados", mas_alejados_bucle, mas_alejados_funciones, mas_alejados_pandas)
coinciden = (
    encima_bucle == encima_funciones == encima_pandas
    and debajo_bucle == debajo_funciones == debajo_pandas
    and mayor_normalizado_bucle == mayor_normalizado_funciones == mayor_normalizado_pandas
    and menor_normalizado_bucle == menor_normalizado_funciones == menor_normalizado_pandas
    and mas_alejados_bucle == mas_alejados_funciones == mas_alejados_pandas
)
print("Coinciden:", coinciden)
print("Lucía es quien más se aleja de la media: 26 puntos, aproximadamente 1,82 desviaciones estándar.")
print("Ninguna puntuación está a más de dos desviaciones estándar de la media.")
print("Conclusión: media de 74, mediana de 75 y moda de 80 puntos.")
print("Siete de los diez alumnos obtienen entre 60 y 80 puntos, ambos incluidos.")

print("\nTabla final de resultados")
print(df[[
    "nombre", "puntos_prueba", "desviacion", "puntos_normalizados", "puntos_estandarizados",
]].to_string(index=False, float_format=lambda valor: f"{valor:.4f}"))
print("\nFin de los ejercicios.")
