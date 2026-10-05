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
print(df1[(df1["Edad"]>= 22) & (df1["Puntos"]>=40)])
print(df1[(df1["Edad"]< 22) & (df1["Estudios superiores"]==True) & (df1["Puntos"]>=35)])



print("*********************************************************************************")
print("******Solución del ejercicio 5******")












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
