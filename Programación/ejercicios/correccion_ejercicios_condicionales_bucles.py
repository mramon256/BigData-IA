# Corrección ejercicio 1

# FALTA SABER NOTA MÁS ALTA Y MÁS BAJA
notas = [5, 9, 8, 6, 4, 10, 8, 4.5, 7, 6]
nota_mas_alta = notas[0]
nota_mas_baja = notas[0]

print("Corrección del ejercicio 1")
for nota in notas:
    if nota > nota_mas_alta:
        nota_mas_alta = nota

    if nota < nota_mas_baja:
        nota_mas_baja = nota

print("Nota más alta:", nota_mas_alta)
print("Nota más baja:", nota_mas_baja)

# Ejercicio 2

print("Mejora del ejercicio 2")
# Como mejora de estilo, puedes guardar el descuento en una variable para que el cálculo sea más legible.
productos = ["pan", "leche", "arroz", "huevos"]
precios = [1.20, 0.95, 10, 15]
total_compra = 0
descuento = 0

for producto, precio in zip(productos, precios):
    print(producto, "tiene un precio de: ", precio, "€")
    total_compra += precio

if total_compra > 20:
    print("Coste total de la compra: ", total_compra, "€")
    descuento = total_compra * 0.10
    total_compra = total_compra - descuento
    print("Coste total con un 10%" , "de descuento: ", total_compra, "€")
else:
    print("Coste total de la compra: ", total_compra, "€")


# Corrección ejercicio 3
print("***********************************************************************************")
print("Solución del ejercicio 3")
alumno = {
    "nombre": "Pablo",
    "edad": 23,
    "curso": "Desarrollo de Aplicaciones en Python",
    "nota_media": 7,
    "faltas": 5
}
print("Datos del alumno:", alumno)
aprueba = alumno["nota_media"] >= 5
recibe_aviso = alumno["faltas"] > 10
for valor in alumno.values():
    print(valor)

if aprueba and recibe_aviso:
    print("El alumno aprueba pero recibe aviso por faltas")
elif aprueba and not recibe_aviso:
    print("El alumno aprueba pero no recibe aviso por faltas")
elif not aprueba and recibe_aviso:
    print("El alumno no aprueba pero recibe aviso por faltas")
else:
    print("El alumno no aprueba y no recibe aviso por faltas")

# Corrección ejercicio 7

# añadir variable encontrado con valor booleano
encontrado = False
alumnos = ["Ana", "Paco", "Marta", "Luis", "Elena", "Carlos", "Sara"]
buscar_nombre = "Carlos"
for posicion, nombre in enumerate(alumnos):
    if nombre == buscar_nombre:
        print("El siguiente nombre está en la posición: ", posicion)
        encontrado = True
        break
else:
    print("Alumno no encontrado")

# Corrección ejercicio 9

# añadir si el usuario es menor de 18 años
usuarios = [
    {
        "nombre": "Luis",
        "edad": 25,
        "activo": False,
        "puntos": 35
    },

    {
        "nombre": "Marta",
        "edad": 16,
        "activo": True,
        "puntos": 41,
    },

    {
        "nombre": "Juan",
        "edad": 32,
        "activo": True,
        "puntos": 56
    },

    {
        "nombre": "Sara",
        "edad": 22,
        "activo": True,
        "puntos": 125 
    }
]
# añadir variable clasificacion tipo string
clasificacion = ""
for usuario in usuarios:
    if usuario["activo"] == True and usuario["puntos"] >= 100:
        clasificacion = "Premium"
    elif usuario["activo"] == True and usuario["puntos"] < 100:
        clasificacion = "Estándar"
    else:
        clasificacion = "Inactivo"
# comprobar si usuario es menor de edad    
    if usuario["edad"] < 18:
        clasificacion += " - usuario menor de edad"

    print(usuario["nombre"], ":", clasificacion)

# Corrección ejercicio 10
codigo_correcto = 2026
# La lista conviene que sea de strings y se tiene que incluir un intento vacío
intentos = ["1234", "5678", "9012", "3456", "7890", "", "2468", "1357"]

# utilizar una variable booleana para recordar si el acceso se ha concedio
acceso_concedido = False

for intento in intentos:
    print("Intento realizado:", intento)
    if intento == "":
        pass
    elif intento == codigo_correcto:
        print("Acceso concedido")
        acceso_concedido = True
        break
    else:
        print("Código incorrecto")

# Acceso denegado no debe imprimirse en cada intento incorrecto, sino solo al final si no se encontró el código correcto.
if not acceso_concedido:
    print("Acceso denegado")



