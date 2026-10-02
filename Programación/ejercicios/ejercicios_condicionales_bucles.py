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
print("Datos del alumno: ")
alumno = {
    "nombre": "Pablo",
    "edad": 23,
    "curso": "Desarrollo de Aplicaciones en Python",
    "nota_media": 7,
    "faltas": 5
}
aprobado = True
recibir_aviso = False
for valor in alumno.values():
    print(valor)

if alumno["nota_media"] >= 5:
    print("¿Alumno aprueba? ", aprobado, " ¿Alumno recibe aviso? ", recibir_aviso)
elif alumno["nota_media"] >= 5 and alumno["faltas"] > 10:
    print("¿Alumno aprueba? ", aprobado, " ¿Alumno recibe aviso? ", recibir_aviso==True)
else:
    print("¿Alumno aprueba? ", not aprobado)


# Ejercicio 4. Números pares, impares y múltiplos
# Usando range, recorre los números del 1 al 50.
# El programa debe:
# - Contar cuántos números son pares.
# - Contar cuántos números son impares.
# - Contar cuántos números son múltiplos de 5.
# - Mostrar los tres resultados finales.
# Condición: Debe utilizar for, range, el operador módulo % y contadores.

# Código de la solución del ejercicio 4
print("***********************************************************************************")
print("Solución del ejercicio 4")

cont_pares = 0
cont_impares = 0
cont_multiplos_cinco = 0
pares = []
impares = []
multiplos_cinco = []
for i in range (1, 51):
    if i % 5 == 0:
        cont_multiplos_cinco = cont_multiplos_cinco + 1
        multiplos_cinco.append(i)
    if i % 2 == 0:
        cont_pares = cont_pares + 1
        pares.append(i)
    else:
        cont_impares = cont_impares + 1
        impares.append(i)

print("Total números pares: ", cont_pares)
print("Total números impares: ", cont_impares)
print("Total números múltiplos de 5: ", cont_multiplos_cinco)
print("Números pares: ", pares)
print("Números impares: ", impares)
print("Múltiplos de 5: ", multiplos_cinco)

# Ejercicio 5. Validación de contraseña
# Crea una variable llamada password con una contraseña de prueba.
# El programa debe:
# - Comprobar si la contraseña tiene al menos 8 caracteres.
# - Comprobar si contiene el símbolo @.
# - Comprobar que no sea igual a 12345678.
# - Si cumple todas las condiciones, mostrar Contraseña válida.
# - En caso contrario, mostrar Contraseña no válida.
# Condición: Debe utilizar strings, len, operadores lógicos y condicionales. Para comprobar si aparece @ dentro del texto puede utilizarse "@" in password.

# Código de la solución del ejercicio 5
print("***********************************************************************************")
print("Solución del ejercicio 5")

password = "Il0v3Pyth0n"
longitud = len(password)
if longitud >= 8 and "@" in password and password != "12345678":
    print("Contraseña válida")
else:
    print("Contraseña no válida")


# Ejercicio 6. Inventario de productos
# Crea un diccionario donde las claves sean nombres de productos y los valores sean las unidades disponibles.
# El programa debe:
# - Mostrar todos los productos y sus unidades.
# - Mostrar qué productos están agotados.
# - Calcular cuántas unidades hay en total.
# - Mostrar cuántos productos tienen menos de 10 unidades.
# Condición: Debe utilizar diccionarios, items(), acumuladores, contadores e if.

# Código de la solución del ejercicio 6
print("***********************************************************************************")
print("Solución del ejercicio 6")  

inventario = {
    "ratón": 12,
    "teclado": 5,
    "monitor": 0,
    "cable": 25
}
suma_unidades = 0
cont_productos = 0

for producto, unidades in inventario.items():
    print (producto, ":", unidades)
    suma_unidades += unidades
    if unidades == 0:
        print("Productos agotados: ", producto)
    elif unidades < 10:
        cont_productos = cont_productos + 1
    else:
        print("El resto de productos tienen más de 10 unidades: ", producto)
print("Total de unidades: ", suma_unidades)
print("Total productos que tienen menos de 10 unidades:", cont_productos)


# Ejercicio 7. Búsqueda en una lista
# Crea una lista de nombres de alumnos y una variable con el nombre que se quiere buscar.
# El programa debe:
# - Recorrer la lista buscando ese nombre.
# - Si encuentra el nombre, mostrar en qué posición está.
# - Cuando lo encuentre, detener la búsqueda.
# - Si no lo encuentra, mostrar Alumno no encontrado.
# Condición: Debe utilizar listas, for, enumerate, if, break y una variable booleana de control.    

alumnos = ["Ana", "Paco", "Marta", "Luis", "Elena", "Carlos", "Sara"]


# Ejercicio 11. Diferencias y similitudes:
# i++ es igual que ++i ?
# i-- es igual que --i?
# i+=1 es igual que i++ ?

# Ejercicio 12. zip y ... en iterables
