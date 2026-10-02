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

df = pd.DataFrame(usuarios)

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
        "Estudios superiores": True
    },
    {
        "Nombre": "Ana",
        "Edad": 23,
        "Puntos": 43,
        "Estudios superiores": True
    },
    {
        "Nombre": "Ana",
        "Edad": 23,
        "Puntos": 43,
        "Estudios superiores": True
    },
    {
        "Nombre": "Ana",
        "Edad": 23,
        "Puntos": 43,
        "Estudios superiores": True
    },
    {
        "Nombre": "Ana",
        "Edad": 23,
        "Puntos": 43,
        "Estudios superiores": True
    },
    {
        "Nombre": "Ana",
        "Edad": 23,
        "Puntos": 43,
        "Estudios superiores": True
    },
    {
        "Nombre": "Ana",
        "Edad": 23,
        "Puntos": 43,
        "Estudios superiores": True
    }
]

print(df)
