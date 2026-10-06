import pandas as pd

#-Diccionario.
#-Lista de Diccionarios.
#-11 listas separadas.
#-Lista de tuplas.


# Ejercicio 1. Crear la estructura de datos
# Crea una estructura de datos en Python que guarde toda la información de la tabla anterior.
# Piensa primero cuál es la forma más cómoda de organizar los datos: una lista para cada columna, un diccionario de listas o una lista de diccionarios.
# Recomendación: usa un diccionario donde cada clave sea una columna.
# - "nombre"
# - "edad"
# - "puntos"
# - "estudios_superiores"
# - Para estudios_superiores, usa valores booleanos: True o False.
dict_candidatos = {
    "Nombre": ["Ana", "Paco", "Marta", "Luis", "Elena", "Carlos", "Sara", "Miguel", "Lucia", "Andres"],
    "Edad": [23, 21, 19, 25, 22, 20, 18, 27, 21, 24],
    "Puntos": [43, 38, 41, 35, 39, 36, 34, 45, 42, 37],
    "Estudios superiores": [True, False, True, False, True, True, False, False, True, False]
}

# Ejercicio 2. Crear un DataFrame
# Importa la librería pandas con el pseudónimo pd.
# Convierte la estructura de datos anterior en un DataFrame.
# Muestra la tabla completa por pantalla.  
print("******Solución del ejercicio 2******")
df1 = pd.DataFrame(dict_candidatos)
print("******DataFrame 1******")
print(df1)
# Ejercicio 3. Explorar el DataFrame
# Usa métodos básicos de pandas para conocer mejor los datos antes de modificarlos.
# Debes mostrar las primeras filas, el tamaño del DataFrame, las columnas, los tipos de datos, la información general y las estadísticas básicas.
# - head()
# - shape
# - columns
# - dtypes
# - info()
# - describe()
print("*********************************************************************************")
print("******Solución del ejercicio 3******")
print("head(): muestra primeras filas")
print(df1.head())
print("shape: muestra número de filas y columnas")
print(df1.shape)
print("columns: muestra los nombres de las columnas")
print(df1.columns)
print("dtypes: muestra los tipos de datos")
print(df1.dtypes)
print("info(): muestra información general de la tabla")
print(df1.info())
print("describe: muestra estadísticas básicas")
print(df1.describe())


# Ejercicio 4. Crear una regla de selección
# Queremos decidir si una persona es apta para el trabajo.
# Antes de programarlo, escribe la lógica con tus propias palabras.
# - Si tiene 22 años o más, será apta si tiene al menos 40 puntos.
# - Si tiene menos de 22 años, solo será apta si tiene estudios superiores y al menos 35 puntos.
# - En cualquier otro caso, no será apta.
print("*********************************************************************************")
print("******Solución del ejercicio 4******")

def es_apto(fila):
    if fila["Edad"] >= 22:
        return fila["Puntos"] >= 40
    
    elif fila["Edad"] < 22:
        return fila["Estudios superiores"] and fila["Puntos"] >= 35
    
    else:
        return False

# Ejercicio 5. Añadir una nueva columna
# Añade al DataFrame una nueva columna llamada apto.
# La columna debe contener True si la persona es apta y False si no lo es.
# Después, muestra el DataFrame completo con la nueva columna.
("*********************************************************************************")
print("******Solución del ejercicio 5******")

df1["Apto"] = df1.apply(es_apto, axis=1)

aptos = df1[df1["Apto"] == True]
print(df1)

# Ejercicio 6. Contar personas aptas y no aptas
# Usa pandas para contar cuántas personas son aptas y cuántas no.
# El objetivo es practicar el recuento de valores dentro de una columna.
# - Método recomendado: value_counts().
("*********************************************************************************")
print("******Solución del ejercicio 6******")
print(df1["Apto"].value_counts())

# Ejercicio 7. Filtrar candidatos aptos
# Crea un nuevo DataFrame llamado candidatos_aptos.
# Debe contener solo las personas que han sido aceptadas para el trabajo.
# Después, muestra esa tabla por pantalla.
("*********************************************************************************")
print("******Solución del ejercicio 7******")
candidatos_aptos = (df1[df1["Apto"] == True])
print(candidatos_aptos)

# Ejercicio 8. Filtrar candidatos con estudios superiores
# Crea otro DataFrame con las personas que tienen estudios superiores.
# Después, responde a las preguntas indicadas.
# - Cuántas personas tienen estudios superiores.
# - Cuántas de ellas son aptas.
# - Hay alguna persona con estudios superiores que no sea apta.
("*********************************************************************************")
print("******Solución del ejercicio 8******")
tiene_estudios_superiores = (df1[df1["Estudios superiores"] == True])
print(tiene_estudios_superiores.value_counts())
print(tiene_estudios_superiores["Apto"].value_counts())

# Ejercicio 9. Ordenar los candidatos
# Ordena el DataFrame por la columna puntos.
# Debes mostrar la tabla ordenada de menor a mayor puntuación y después de mayor a menor puntuación.
# - Método recomendado: sort_values().
("*********************************************************************************")
print("******Solución del ejercicio 9******")
print("******Tabla ordenada de menor a mayor******")
print(df1.sort_values("Puntos"))
print("******Tabla ordenada de mayor a menor******")
print(df1.sort_values("Puntos", ascending=False))

# Ejercicio 10. Calcular estadísticas
# Calcula estadísticas básicas usando pandas.
# Estas operaciones ayudan a interpretar los datos antes de tomar decisiones.
# - Edad media.
# - Puntuación media.
# - Puntuación máxima.
# - Puntuación mínima.
# - Edad de la persona más joven.
# - Edad de la persona más mayor.
# - Métodos útiles: mean(), max(), min().
("*********************************************************************************")
print("******Solución del ejercicio 10******")
print("Edad media:", df1["Edad"].mean())
print("Puntuación media:", df1["Puntos"].mean())
print("Puntuación máxima:", df1["Puntos"].max())
print("Edad persona más joven:", df1["Edad"].min())
print("Edad persona más mayor:", df1["Edad"].max())

# Ejercicio 11. Crear una columna de nivel
# Añade una nueva columna llamada nivel.
# La columna debe clasificar a cada persona según sus puntos.
# - "alto" si tiene 40 puntos o más.
# - "medio" si tiene entre 35 y 39 puntos.
# - "bajo" si tiene menos de 35 puntos.
("*********************************************************************************")
print("******Solución del ejercicio 11******")
df1["nivel"] = "bajo"
df1.loc[df1["Puntos"] >= 40, "nivel"] = "alto"
df1.loc[(df1["Puntos"] >= 35) & (df1["Puntos"] < 40), "nivel"] = "medio"
print(df1["nivel"])
# Ejercicio 12. Agrupar por nivel
# Agrupa los datos por la columna nivel.
# Calcula cuántas personas hay en cada nivel, la media de edad en cada nivel y la media de puntos en cada nivel.
# - Método recomendado: groupby().
("*********************************************************************************")
print("******Solución del ejercicio 12******")
grupo = df1.groupby("nivel")
print("Total personas en cada nivel")
print(grupo["Nombre"].count())
print("Media de edad en cada nivel")
print(grupo["Edad"].mean())
print("Media de puntos en cada nivel")
print(grupo["Puntos"].mean())

# Ejercicio 13. Seleccionar columnas concretas
# Crea un nuevo DataFrame que solo contenga las columnas nombre, puntos y apto.
# Este ejercicio sirve para practicar cómo seleccionar solo la información importante.
("*********************************************************************************")
print("******Solución del ejercicio 13******")
nuevo_df = df1[["Nombre", "Puntos", "Apto"]]
print(nuevo_df)

# Ejercicio 14. Renombrar columnas
# Renombra las columnas para que tengan nombres más descriptivos.
# Por ejemplo, nombre puede pasar a Nombre del candidato y puntos a Puntuación.
# - Método recomendado: rename().
("*********************************************************************************")
print("******Solución del ejercicio 14******")

nuevo_df_modificado = nuevo_df.rename(columns={"Nombre" : "Nombre del candidato", "Puntos" : "Puntuación", "Apto" : "Candidato apto"})
print(nuevo_df_modificado)



print("******RESTO DE DATAFRAMES******")
lista1_candidatos = [
    {
        "Nombre": "Ana",
        "Edad": 23,
        "Puntos": 43,
        "Estudios superiores": True
    },
    {
        "Nombre": "Paco",
        "Edad": 21,
        "Puntos": 38,
        "Estudios superiores": False
    },
    {
        "Nombre": "Marta",
        "Edad": 19,
        "Puntos": 41,
        "Estudios superiores": True
    },
    {
        "Nombre": "Luis",
        "Edad": 25,
        "Puntos": 35,
        "Estudios superiores": False
    },
    {
        "Nombre": "Elena",
        "Edad": 22,
        "Puntos": 39,
        "Estudios superiores": True
    },
    {
        "Nombre": "Carlos",
        "Edad": 20,
        "Puntos": 36,
        "Estudios superiores": True
    },
    {
        "Nombre": "Sara",
        "Edad": 18,
        "Puntos": 34,
        "Estudios superiores": False
    },
    {
        "Nombre": "Miguel",
        "Edad": 27,
        "Puntos": 45,
        "Estudios superiores": False
    },
    {
        "Nombre": "Lucia",
        "Edad": 21,
        "Puntos": 42,
        "Estudios superiores": True
    },
    {
        "Nombre": "Andres",
        "Edad": 24,
        "Puntos": 37,
        "Estudios superiores": False
    }
]

df2 = pd.DataFrame(lista1_candidatos)
#print("******DataFrame 2******")
#print(df2)

cabecera = ["Nombre", "Edad", "Puntos", "Estudios superiores"]
candidato1 = ["Ana", 23, 43, True]
candidato2 = ["Paco", 21, 38, False]
candidato3 = ["Marta", 19, 41, True]
candidato4 = ["Luis", 25, 35, False]
candidato5 = ["Elena", 22, 39, True]
candidato6 = ["Carlos", 20, 36, True]
candidato7 = ["Sara", 18, 34, False]
candidato8 = ["Miguel", 27, 45, False]
candidato9 = ["Lucia", 21, 42, True]
candidato10 = ["Andres", 24, 37, False]

df3 = pd.DataFrame([
    candidato1,
    candidato2,
    candidato3,
    candidato4,
    candidato5,
    candidato6,
    candidato7,
    candidato8,
    candidato9,
    candidato10,
], columns=cabecera)
#print("******DataFrame 3******")
#print(df3)

lista2_candidatos = [
    ("Ana", 23, 43, True),
    ("Paco", 21, 38, False),
    ("Marta", 19, 41, True),
    ("Luis", 25, 35, False),
    ("Elena", 22, 39, True),
    ("Carlos", 20, 36, True),
    ("Sara", 18, 34, False),
    ("Miguel", 27, 45, False),
    ("Lucia", 21, 42, True),
    ("Andres", 24, 37, False),
]

df4 = pd.DataFrame(lista2_candidatos, columns=("Nombre", "Edad", "Puntos", "Estudios superiores"))
#print("******DataFrame 4******")
#print(df4) 
