<<<<<<< HEAD
# Ejercicio 1. Control de notas
# Crea una lista llamada notas con al menos 10 calificaciones numéricas.
# El programa debe:
# - Mostrar todas las notas.
# - Calcular cuántas notas están aprobadas y cuántas suspendidas.
# - Calcular la nota media.
# - Mostrar la nota más alta y la nota más baja.
# - Indicar si la media final está aprobada o suspendida.
# Condición: Debe utilizar listas, bucle for, operadores de comparación y condicionales.

# Código de la solución del ejercicio 1
notas = [5, 9, 8, 6, 4, 9, 8, 4.5, 7, 6]
aprobadas = 0
suspendidas = 0
suma_notas = 0
nota_media = 0
mensaje = ""

print("Solución del ejercicio 1")
print("Lista notas: ", end="")
for nota in notas:
    print(nota, end=", ")
    suma_notas += nota
    if nota >= 5:
        aprobadas = aprobadas + 1
    else:
        suspendidas = suspendidas + 1
else:
    nota_media = suma_notas / (aprobadas + suspendidas)
    mensaje = "Aprobada" if nota_media >= 5 else "Suspendida"
print("Notas aprobadas: ", aprobadas)
print("Notas suspendidas: ", suspendidas)
print("Nota media: ", nota_media)
# FALTA SABER NOTA MÁS ALTA Y MÁS BAJA
print("Total suma notas: ", suma_notas)
print("Resultado media final:", mensaje)

# Ejercicio 2. Carrito de la compra
# Crea dos listas: una con nombres de productos y otra con sus precios.
# El programa debe:
# - Mostrar cada producto con su precio.
# - Calcular el precio total de la compra.
# - Aplicar un descuento del 10% si el total supera 20 euros.
# - Mostrar el total final que debe pagarse.
# Condición: Debe utilizar zip, un acumulador, if y operadores aritméticos.

# Código de la solución del ejercicio 2 
productos = ["pan", "leche", "arroz", "huevos"]
precios = [1.20, 0.95, 10, 15]
total_compra = 0

print("***********************************************************************************")
print("Solución del ejercicio 2")
for producto, precio in zip(productos, precios):
    print(producto, "tiene un precio de: ", precio, "€")
    total_compra += precio

if total_compra > 20:
    print("Coste total de la compra: ", total_compra, "€")
    total_compra = total_compra - (total_compra *(10/100))
    print("Coste total con un 10%" , "de descuento: ", total_compra, "€")
else:
    print("Coste total de la compra: ", total_compra, "€")

# Ejercicio 3. Registro de alumno
# Crea un diccionario llamado alumno con los siguientes datos:
# nombre, edad, curso, nota_media, faltas
# El programa debe:
# - Mostrar todos los datos del alumno.
# - Indicar si el alumno aprueba. Aprueba si su nota_media es mayor o igual que 5.
# - Indicar si debe recibir un aviso. Recibe aviso si tiene más de 10 faltas.
# - Mostrar un mensaje final combinando el resultado académico y el aviso por faltas.
# Condición: Debe utilizar diccionarios, if, elif, else y operadores lógicos.

# Código de la solución del ejercicio 3
print("***********************************************************************************")
print("Solución del ejercicio 3")
print("Estos son los valores del alumno: ", end="")
alumno = {
    "nombre": "Pablo",
    "edad": 23,
    "curso": "Desarrollo de Aplicaciones en Python",
    "nota_media": 7,
    "faltas": 5
}
for valor in alumno.values():
    print(valor, end=", ")

    if alumno["nota_media"] >= 5:
        print("Alumno aprueba")
 



# Ejercicio 11. Diferencias y similitudes:
# i++ es igual que ++i ?
# i-- es igual que --i?
# i+=1 es igual que i++ ?

=======
# Ejercicio 1. Control de notas
# Crea una lista llamada notas con al menos 10 calificaciones numéricas.
# El programa debe:
# - Mostrar todas las notas.
# - Calcular cuántas notas están aprobadas y cuántas suspendidas.
# - Calcular la nota media.
# - Mostrar la nota más alta y la nota más baja.
# - Indicar si la media final está aprobada o suspendida.
# Condición: Debe utilizar listas, bucle for, operadores de comparación y condicionales.

# Código de la solución del ejercicio 1
notas = [5, 9, 8, 6, 4, 9, 8, 4.5, 7, 6, 4]
aprobadas = 0
suspendidas = 0
for nota in notas:
    print("Estas son las notas: ", nota)
    if nota >= 5:
        aprobadas = aprobadas + 1
    else:
        suspendidas = suspendidas + 1

print("Solución del ejercicio 1")
#print("Estas son las notas: ", nota)
print("Notas aprobadas: ", aprobadas)
print("Notas suspendidas: ", suspendidas)
print("Nota media: ", (aprobadas + suspendidas))



# Ejercicio 11. Diferencias y similitudes:
# i++ es igual que ++i ?
# i-- es igual que --i?
# i+=1 es igual que i++ ?

>>>>>>> c6c0151035160dc499c2b63415ccfb5ed4cfd4e8
# Ejercicio 12. "zip" y "enumerate" en iterables