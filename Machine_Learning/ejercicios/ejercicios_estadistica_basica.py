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

# Cada fila representa un alumno en el que se le ha registrado sus horas de estudio, los puntos recibidos sobre 100 en una prueba, el número de ejercicios que ha entregado y el total de minutos que ha estado conectado a la plataforma en un día concreto

print("***Solución del ejercicio 1***")
df = pd.read_csv("Machine_Learning/ejercicios/datos_estadistica_alumnos.csv")
puntos = df["puntos_prueba"]
filas = df.to_dict("records")

# Método 1: bucles
print("***MÉTODO 1***")
print("Primeras cinco filas con un bucle:")
for i in range(5):
    print(filas[i])

cont_puntos = 0

# Bucle para averiguar cuantos valores hay en la columna puntos_prueba
for valor in puntos:
    cont_puntos = cont_puntos + 1

print("Total de valores en la columna puntos:", cont_puntos)

# Método 2: funciones
print("***MÉTODO 2***")
print("Primeras cinco filas con funciones de Python:")
print(filas[:5])

# Función para contar valores de la columna puntos_prueba
def contar_puntos(puntos):
    cont_puntos = 0

    for valor in puntos:
        cont_puntos = cont_puntos + 1

    return cont_puntos
# Llamar a la función
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

# En este contexto, la media representa la nota promedio del conjunto de alumnos, calculada mediante la suma de todas las puntuaciones dividida entre el número de alumnos.

# Método 1: bucles
print("***MÉTODO 1***")
# Cálculo de la media
suma = 0
for valor in puntos:
    suma += valor
media_bucle = suma / len(puntos)
print("Media puntos:", media_bucle)

# Método 2: funciones
print("***MÉTODO 2***")
# Función que cálcula la media
def calcular_media(puntos):
    media = sum(puntos) / len(puntos)

    # Devolver la media calculada
    return media

# Llamar a la función y guardar el resultado
media_funciones = calcular_media(puntos)

# Función lambda que calcula la media
# map() sirve para aplicar la función lambda a cada elemento de un iterable (recorre columna puntos_prueba)
# sum() suma los valores obtenidos
media_funcion_lambda = sum(map(lambda x: x, puntos)) / len(puntos)

# Mostrar el resultado
print("Media puntos:", media_funciones)
print("Media puntos:", media_funcion_lambda)

# Método 3: pandas
print("***MÉTODO 3***")
# el método mean() devuelve la media de los valores de la columna puntos_prueba
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

# La mediana representa el centro de los datos porque, una vez ordenados, se dividen en dos mitades y queda la misma cantidad a cada lado.

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
# Uso de dos bucles para comparar un elemento con todos sus posteriores
# Cada elemento es "i" una vez, que se compara con "j" que equivale a todos los elementos posteriores de "i"
# Cuando "j" llega al último elemento de lista_puntos, "i" pasa a corresponder al siguiente elemento del de donde estaba
for i in range(len(lista_puntos)):
    for j in range(i+1, len(lista_puntos)):
        if lista_puntos[i] > lista_puntos[j]:
            aux = lista_puntos[i]
            # variable aux guarda el valor "i" de forma temporal
            lista_puntos[i] = lista_puntos[j]
            lista_puntos[j] = aux
            
# Buscar los valores centrales
for punto in lista_puntos:
    # variable posicion indexa los elementos de lista_puntos
    # calculo para saber el valor que se encuentra en la posicion anterior al valor central 
    if posicion == (cont_puntos//2) - 1:
        punto_anterior = punto
    if posicion == cont_puntos//2:
        punto_central = punto
    posicion += 1

# Si el número de puntos es par
if cont_puntos % 2 == 0:
    # se obtiene la mediana sumando el valor central con su elemento anterior y dividiendo el resultado entre 2
    mediana_bucle = (punto_anterior + punto_central)/2
    print("Mediana:",mediana_bucle)

# Si el número de puntos es impar
else:
    for punto in lista_puntos:
        # cuando el valor de posicion es equivalente a la mitad de la lista, el elemento en esa posicion es la mediana
        if posicion == (cont_puntos//2):
            mediana_bucle = punto
            print("Mediana:",mediana_bucle)
        posicion += 1

# Método 2: funciones
print("***MÉTODO 2***")
# Función para calcular la mediana
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
        # función sorted() ordena los elementos de la lista de menor a mayor
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

# La moda es el valor que más se repite

# Método 1: bucles
print("***MÉTODO 1***")
cont_iguales = 1 # contador inicializado en 1 ya que cada elemento ya aparece 1 vez 
cant_mayor = 0
moda_bucle = 0
frecuencias = {} # diccionario que almacenará cada valor y las veces aparece

# bucle que recorre las posiciones de lista_puntos
for i in range (len(lista_puntos)):
    # Comprobar si cada valor de lista_puntos[i] no está entre las claves del diccionario frecuencias
    if lista_puntos[i] not in frecuencias:
        # Reiniciar contador 
        cont_iguales = 1

        # segundo bucle en el que se compara el elemento de la posición "i" con sus posteriores  
        for j in range(i+1, len(lista_puntos)):
            # Cada elemento es "i" una vez, que se compara con "j" que equivale a todos los elementos posteriores de "i"
            # Cuando "j" llega al último elemento de lista_puntos, "i" pasa a corresponder al siguiente elemento del de donde estaba
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

    # Función lambda que busca el valor que aparece más veces en la lista (Solucionado utilizando la web w3.schools).
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

# La desviación indica cuánto se aleja un valor de la media. Si la desviación es positiva es que está por encima de la media, si es negativa es que está por debajo de la media y si la desviación es 0 es que está exactamente en la media.

# Método 1: bucles
print("***MÉTODO 1***")
print("Desviación:")
suma = 0
calculo_desviacion = 0
lista_desviacion = []
# Cálculo de la media
for punto in puntos:
    suma += punto
media_bucle = suma / len(puntos)

# segundo bucle para calcular la desviación respecto a la media
for punto in puntos:
    # se cálcula restando cada elemento de la columna puntos_prueba, con la media
    calculo_desviacion = punto - media_bucle
    # añadimos con append() el resultado de la desviacion de cada punto a una lista
    lista_desviacion.append(calculo_desviacion)
print(lista_desviacion)

# Método 2: funciones
print("***MÉTODO 2***")
print("Desviación:")
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
# Crear nueva columna llamada desviacion
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

# La varianza mide el promedio de las desviaciones al cuadrado respecto a la media

# Método 1: bucles
print("***MÉTODO 1***")
suma = 0
suma_desviacion = 0
cont_desviacion = 0
# Cálculo de la media
for valor in puntos:
    suma += valor
media_bucle = suma / len(puntos)


for punto in puntos:
    desviacion = punto - media_bucle # Cálculo de la desviación
    desviacion_elevada = desviacion * desviacion # desviación de cada punto al cuadrado
    suma_desviacion += desviacion_elevada # sumar los resultados de las desviaciones al cuadrado
    cont_desviacion = cont_desviacion + 1 # contar elementos
    
    # obtener varianza diviendo el resultado del acumulador entre la cantidad de valores
    varianza_bucle = suma_desviacion / cont_desviacion
print("Varianza:", varianza_bucle)

# Método 2: funciones
print("***MÉTODO 2***")
def calcular_varianza(puntos):
    # Calcular la media utilizando map(), lambda, sum() y len()
    media_funciones = sum(map(lambda x: x, puntos)) / len(puntos)

    # Calcular la suma de las desviaciones al cuadrado
    suma_desviacion = sum(map(lambda x: (x - media_funciones) ** 2, puntos))

    # Calcular la varianza dividiendo entre el número de elementos
    varianza_funciones = suma_desviacion / len(puntos)

    # Devolver la varianza calculada
    return varianza_funciones


# Llamar a la función y guardar el resultado
varianza_funciones = calcular_varianza(puntos)

# Mostrar la varianza
print("Varianza:", varianza_funciones)

# Método 3: pandas
print("***MÉTODO 3***")
varianza_pandas = df["puntos_prueba"].var(ddof=0)
print("Varianza:", varianza_pandas)

# Ejercicio 7. Desviación estándar
# - Calcula la desviación estándar con el Método 1: parte de la varianza calculada con bucles y aplica la raíz cuadrada.
# - Calcula la misma desviación estándar con el Método 2: usa map(), lambda, sum(), len() y raíz cuadrada.
# - Calcula la misma desviación estándar con el Método 3: pandas usando .std(ddof=0).
# - Muestra los tres resultados con nombres claros: desviacion_estandar_bucle, desviacion_estandar_funciones y desviacion_estandar_pandas.
# - Comprueba que los tres resultados coinciden o que solo cambian por pequeños decimales.
# - Explica por qué la desviación estándar es más fácil de interpretar que la varianza. 
# Pandas que puedes usar: df["puntos_prueba"].std(ddof=0).
print("***Solución del ejercicio 7***")

# La desviación estándar expresa las mismas unidades que los datos originales. La varianza en cambio, se expresa en unidades al cuadrado

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

# Bucle que calcula los cuadrados de los números del 1 al 15.
# De esta manera, comprobé que la varianza (204) se encuentra entre los cuadrados de 14 (196) y 15 (225).
for i in range(1, 15+1):
    cuadrado = i*i
    print (i, "al cuadrada es:", cuadrado)

# cálculo de la desviación estándar.
# para clacular la raíz cuadrada se eleva la cifra a la potencia de un medio (0.5)
desviacion_estandar_bucle = varianza_bucle ** 0.5
# .2f muestra los dos primeros decimales de una cifra
print(f"Desviación estándar: {desviacion_estandar_bucle:.2f}")

# Método 2: funciones
print("***MÉTODO 2***")
# Función para calcular la media
def calcular_media(puntos):
    return sum(puntos) / len(puntos)

# Función para calcular la desviación estándar
def calcular_desviacion_estandar(puntos):
    # Llamar a la función que calcula la varianza
    varianza = calcular_varianza(puntos)
    desviacion_estandar = varianza ** 0.5
    return desviacion_estandar

# Llamada a la función
desviacion_estandar_funciones = calcular_desviacion_estandar(puntos)

print(f"Desviación estándar: {desviacion_estandar_funciones:.2f}")

# Método 3: pandas
print("***MÉTODO 3***")
desviacion_estandar_pandas = df["puntos_prueba"].std(ddof=0)
print(f"Desviación estándar: {desviacion_estandar_pandas:.2f}")

# Ejercicio 8. Normalización min-max
# - Calcula el mínimo y el máximo de puntos_prueba.
# - Normaliza cada valor con el Método 1: bucle for y append(), usando la fórmula (valor - mínimo) / (máximo - mínimo).
# - Normaliza los mismos valores con el Método 2: min(), max(), map() y lambda.
# - Normaliza los mismos valores con el Método 3: pandas usando .min(), .max() y operaciones sobre columnas. Crea una columna llamada puntos_normalizados.
# - Muestra las tres versiones y comprueba que contienen los mismos valores.
# - Explica qué significa que un valor normalizado sea 0, 0.5 o 1.
# Pandas que puedes usar: min(), max() y operaciones directas sobre columnas.
print("***Solución del ejercicio 8***")

# Al normalizar un conjunto de datos, se transforman los valores originales para que queden dentro de un rango fijo.
# 0 equivale al valor mínimo, 0.5 al punto medio de ese rango y 1 al valor máximo

# Método 1: bucles
print("***MÉTODO 1***")
print("Valores normalizados:")
minimo_puntos = puntos[0]
maximo_puntos = puntos[0]

# Bucle para encontrar la puntuación mínima y la máxima
for punto in puntos:
    if punto > maximo_puntos:
        maximo_puntos = punto
    if punto < minimo_puntos:
        minimo_puntos = punto

# Crear una lista vacía para guardar los valores normalizados
lista_normalizada = []

# Recorrer de nuevo la lista para calcular la normalización
for punto in puntos:    
    valor_normalizado_bucle = (punto - minimo_puntos) / (maximo_puntos - minimo_puntos)
    # añadir los valores normalizados a la lista anterior
    # uso de la float() para convertir los valores de tipo numpy.float64 a float nativos de Python
    lista_normalizada.append(float(valor_normalizado_bucle))
print(lista_normalizada)
    
# Método 2: funciones
print("***MÉTODO 2***")
print("Valores normalizados:")
# Función para obtener el valor mínimo
def calcular_minimo(puntos):
    return min(puntos)

# Función para obtener el valor máximo
def calcular_maximo(puntos):
    return max(puntos)

# Obtener el mínimo y el máximo
minimo_funciones = calcular_minimo(puntos)
maximo_funciones = calcular_maximo(puntos)

# Normalizar los valores utilizando map() y lambda
valor_normalizado_funciones = map(
    lambda punto: (punto - minimo_funciones) / (maximo_funciones - minimo_funciones),
    puntos
)

# Mostrar los valores normalizados
# * desempaqueta los elementos de un iterable para que se muestren por separado
# parámetro "sep" establece separador entre argumentos
# "\n" representa salto de línea
print(*valor_normalizado_funciones, sep="\n")

# Método 3: pandas
print("***MÉTODO 3***")
minimo_puntos = df["puntos_prueba"].min()
maximo_puntos = df["puntos_prueba"].max()
valor_normalizado_pandas = df["puntos_normalizados"] = (df["puntos_prueba"] - minimo_puntos) / (maximo_puntos - minimo_puntos)
print("Valores normalizados:", valor_normalizado_pandas)

# Ejercicio 9. Estandarización z-score
# - Calcula la media y la desviación estándar de puntos_prueba.
# - Estandariza cada valor con el Método 1: bucle for y append(), usando la fórmula z = (valor - media) / desviación estándar.
# - Estandariza los mismos valores con el Método 2: map(), lambda y las variables media y desviación estándar ya calculadas.
# - Estandariza los mismos valores con el Método 3: pandas usando .mean(), .std(ddof=0) y operaciones sobre columnas. Crea una columna llamada puntos_estandarizados.
# - Muestra las tres versiones y comprueba que contienen los mismos valores.
# - Explica qué significa que un valor z sea positivo, negativo o cercano a 0.
# Pandas que puedes usar: mean(), std(ddof=0) y operaciones directas sobre columnas.
print("***Solución del ejercicio 9***")

# z = 0 significa que el dato está en la media, z positivo significa que está por encima y z negativo significa que está por debajo.

# Método 1: bucles
print("***MÉTODO 1***")
print("Valor z:")
suma = 0
suma_desviacion = 0
cont_desviacion = 0
lista_valores_z = []
for valor in puntos:
    suma += valor
media_bucle = suma / len(puntos)
for punto in puntos:
    desviacion = punto - media_bucle
    desviacion_elevada = desviacion * desviacion
    suma_desviacion += desviacion_elevada
    cont_desviacion = cont_desviacion + 1
    varianza_bucle = suma_desviacion / cont_desviacion
    desviacion_estandar_bucle = varianza_bucle ** 0.5

# Recorrer de nuevo la lista para calcular la estandarización
for punto in puntos:
    z_bucles = (punto - media_bucle) / desviacion_estandar_bucle
    # uso de "round, 2" para obtener los primeros 2 decimales
    lista_valores_z.append(round(float(z_bucles), 2))
print(lista_valores_z)

# Método 2: funciones
print("***MÉTODO 2***")
print("Valor z:")
# Función para calcular la media
def calcular_media(puntos):
    return sum(puntos) / len(puntos)

# Función para calcular la varianza
def calcular_varianza(puntos):
    media = calcular_media(puntos)
    suma_desviacion = sum(map(lambda punto: (punto - media) ** 2, puntos))
    return suma_desviacion / len(puntos)

# Función para calcular el z-score
def calcular_z_score(puntos):
    media = calcular_media(puntos)
    varianza = calcular_varianza(puntos)
    desviacion_estandar = varianza ** 0.5

    z_score = map(
        lambda punto: (punto - media) / desviacion_estandar,
        puntos
    )

    return z_score

# Llamada a la función
z_score_funciones = calcular_z_score(puntos)

# Mostrar los valores estandarizados
print(*map(lambda valor: f"{valor:.2f}", calcular_z_score(puntos)), sep="\n")


# Método 3: pandas
print("***MÉTODO 3***")
desviacion_estandar_pandas = df["puntos_prueba"].std(ddof=0)
media_pandas = df["puntos_prueba"].mean() 
z_pandas = df["puntos_estandarizados"] = ((df["puntos_prueba"] - media_pandas) / desviacion_estandar_pandas).round(2)
# Uso de round(2) para mostrar los valores con dos decimales
print ("Valor z:", z_pandas.round(2))


# Ejercicio 10. Interpretación final
# - Indica qué alumnos están por encima de la media usando el Método 1: bucle for y condicional.
# - Indica los mismos alumnos usando el Método 2: filter() y lambda.
# - Indica los mismos alumnos usando el Método 3: filtrado de pandas con condiciones sobre columnas.
# - Indica qué alumnos están por debajo de la media usando también los tres métodos.
# - Indica qué alumno o alumnos tienen el valor normalizado más alto.
# - Indica qué alumno o alumnos tienen el valor normalizado más bajo.
# - Indica si hay algún valor que parezca especialmente alejado del resto.
# - Escribe una conclusión breve sobre el rendimiento general del grupo.
print("***Solución del ejercicio 10***")
# Método 1: bucles
print("***MÉTODO 1***")
print("Alumnos con puntos por encima de la media")
for i in range(len(puntos)):
    if puntos[i] > media_bucle:
        # .iloc[i] obtiene el nombre del alumno que ocupa esa misma posición
        print(df["nombre"].iloc[i], puntos[i])

print("Alumnos con puntos por debajo de la media")
for i in range(len(puntos)):
    if puntos[i] < media_bucle:
        print(df["nombre"].iloc[i], puntos[i])

# Bucle para encontrar el valor normalizado más alto y más bajo
valores_normalizados = df["puntos_normalizados"]
valor_normalizado_max = valores_normalizados[0]
valor_normalizado_min = valores_normalizados[0]
for n in range(len(valores_normalizados)):
    if valores_normalizados[n] > valor_normalizado_max:
        valor_normalizado_max = valores_normalizados[n]

    if valores_normalizados[n] < valor_normalizado_min:
        valor_normalizado_min = valores_normalizados[n]

# Mostrar los alumnos con el valor normalizado más alto y más bajo
for n in range(len(valores_normalizados)):
    if valores_normalizados[n] == valor_normalizado_max:
        print("Alumnos con valor normalizado más alto:")
        print(df["nombre"].iloc[n], valores_normalizados[n])

    if valores_normalizados[n] == valor_normalizado_min:
        print("Alumnos con valor normalizado más bajo:")
        print(df["nombre"].iloc[n], valores_normalizados[n])


# Método 2: funciones
print("***MÉTODO 2***")
# Función para mostrar los alumnos por encima de la media
def alumnos_encima_media(puntos):
    media = calcular_media(puntos)
    # "lambda i: puntos[i] > media" comprueba si la puntuación que hay en la posición i es superior a la media
    # filter() obtiene la posición de los elementos que cumplen con la condición anterior
    # range(len(puntos)) genera las posiciones
    alumnos = filter(lambda i: puntos[i] > media, range(len(puntos)))

    print("Alumnos con puntos por encima de la media")
    # map() aplica una función a cada elemento de un iterable y devuelve resultados. En este caso se aplica la función a cada posición "i" que contiene alumnos
    # .iloc[i] accede al nombre situado en la posición i de cada columna
    # puntos[i] obtiene la puntuación correspondiente  
    print(*map(lambda i: f"{df['nombre'].iloc[i]} {puntos[i]}", alumnos), sep="\n")

# Función para mostrar los alumnos por debajo de la media
def alumnos_debajo_media(puntos):
    media = calcular_media(puntos)
    alumnos = filter(lambda i: puntos[i] < media, range(len(puntos)))

    print("Alumnos con puntos por debajo de la media")
    print(*map(lambda i: f"{df['nombre'].iloc[i]} {puntos[i]}", alumnos), sep="\n")

# Llamar a las funciones
alumnos_encima_media(puntos)
alumnos_debajo_media(puntos)

# Función para obtener el valor mínimo
def calcular_minimo(puntos):
    return min(puntos)


# Función para obtener el valor máximo
def calcular_maximo(puntos):
    return max(puntos)


# Función para normalizar los valores
def calcular_normalizacion(puntos):
    minimo = calcular_minimo(puntos)
    maximo = calcular_maximo(puntos)

    return list(map(
        lambda punto: (punto - minimo) / (maximo - minimo),
        puntos
    ))

# Función para encontrar los valores normalizados más alto y más bajo
def encontrar_valores_normalizados(df):
    # .tolist() sirve para convertir una columna de pandas en una lista Python
    puntos = df["puntos_prueba"].tolist()

    # Calcular la normalización utilizando la función anterior
    valores_normalizados = calcular_normalizacion(puntos)

    # Buscar el valor normalizado máximo y mínimo sin min() ni max()
    valor_normalizado_max = valores_normalizados[0]
    valor_normalizado_min = valores_normalizados[0]

    for n in range(len(valores_normalizados)):
        if valores_normalizados[n] > valor_normalizado_max:
            valor_normalizado_max = valores_normalizados[n]

        if valores_normalizados[n] < valor_normalizado_min:
            valor_normalizado_min = valores_normalizados[n]

    # Encontrar los alumnos con el valor normalizado más alto
    alumnos_max = filter(
        lambda n: valores_normalizados[n] == valor_normalizado_max,
        range(len(valores_normalizados))
    )

    print("Alumnos con valor normalizado más alto:")
    print(*map(
        lambda n: f"{df['nombre'].iloc[n]} {valores_normalizados[n]}",
        alumnos_max
    ), sep="\n")

    # Encontrar los alumnos con el valor normalizado más bajo
    alumnos_min = filter(
        lambda n: valores_normalizados[n] == valor_normalizado_min,
        range(len(valores_normalizados))
    )

    print("Alumnos con valor normalizado más bajo:")
    print(*map(
        lambda n: f"{df['nombre'].iloc[n]} {valores_normalizados[n]}",
        alumnos_min
    ), sep="\n")


# Llamar a la función
encontrar_valores_normalizados(df)

# Método 3: pandas
print("***MÉTODO 3***")
print("Alumnos con puntos por encima de la media")
# Crear un DataFrame con los alumnos que superan la media
small_df = df.loc[df["puntos_prueba"] > media_pandas, ["nombre", "puntos_prueba"]]
print(small_df)

print("Alumnos con puntos por debajo de la media")
small_df = df.loc[df["puntos_prueba"] < media_pandas, ["nombre", "puntos_prueba"]]
print(small_df)

# Encontrar los alumnos con el valor normalizado más alto
print("Alumnos con valor normalizado más alto:")
small_df = df.loc[df["puntos_normalizados"] == df["puntos_normalizados"].max(), ["nombre", "puntos_normalizados"]]
print(small_df)

# Encontrar los alumnos con el valor normalizado más bajo
print("Alumnos con valor normalizado más bajo:")
small_df = df.loc[df["puntos_normalizados"] == df["puntos_normalizados"].min(), ["nombre", "puntos_normalizados"]]
print(small_df)


# Conclusión sobre rendimiento del grupo

# En general, el rendimiento del grupo es bastante semejante, ya que las puntuaciones se encuentran relativamente próximas entre sí y no se observan valores extremos. Destacar que 7 alumnos comparten puntuación con algún compañero: 2 alumnos tienen 60 puntos, 2 alumnos con 70 y 3 alumnos con 80. Por otro lado, existe una diferencia considerable entre la puntuación mínima y la máxima, siendo esta última el doble de la primera. Esta diferencia refleja cierta dispersión en los resultados y se tiene en cuenta en el cálculo de la desviación estándar y de las puntuaciones estandarizadas (z-score).

