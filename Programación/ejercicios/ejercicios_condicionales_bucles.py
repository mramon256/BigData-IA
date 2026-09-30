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

# Ejercicio 12. "zip" y "enumerate" en iterables