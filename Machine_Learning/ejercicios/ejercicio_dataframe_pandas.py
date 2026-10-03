import pandas as pd

#-Diccionario.
#-Lista de Diccionarios.
#-11 listas separadas.
#-Lista de tuplas.

usuarios = {
    "Nombre": ["Ana", "Paco", "Marta", "Luis", "Elena", "Carlos", "Sara", "Miguel", "Lucia", "Andres"],
    "Edad": [23, 21, 19, 25, 22, 20, 18, 27, 21, 24],
    "Puntos": [43, 38, 41, 35, 39, 36, 34, 45, 42, 37],
    "Estudios": [True, False, True, False, True, True, False, False, True, False]
}

df1 = pd.DataFrame(usuarios)
print("******DataFrame 1******")
print(df1)

usuarios = [
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

df2 = pd.DataFrame(usuarios)
print("******DataFrame 2******")
print(df2)

cabecera = ["Nombre", "Edad", "Puntos", "Estudios superiores"]
usuario1 = ["Ana", 23, 43, True]
usuario2 = ["Paco", 21, 38, False]
usuario3 = ["Marta", 19, 41, True]
usuario4 = ["Luis", 25, 35, False]
usuario5 = ["Elena", 22, 39, True]
usuario6 = ["Carlos", 20, 36, True]
usuario7 = ["Sara", 18, 34, False]
usuario8 = ["Miguel", 27, 45, False]
usuario9 = ["Lucia", 21, 42, True]
usuario10 = ["Andres", 24, 37, False]

df3 = pd.DataFrame(usuarios)
print("******DataFrame 3******")
print(df3)

usuarios = [
    ("Nombre", "Edad", "Puntos", "Estudios superiores"),
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

df4 = pd.DataFrame(usuarios)
print("******DataFrame 4******")
print(df4)
