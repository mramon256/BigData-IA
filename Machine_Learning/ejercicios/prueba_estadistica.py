lista_puntos = [5, 9, 8, 6, 4, 10, 8, 4.5, 7, 6, 13]
cont_puntos = 0
posicion = 0
punto_anterior = 0
punto_central = 0
mediana_bucle = 0

# Guardar los puntos en una lista y contarlos
for punto in lista_puntos:
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
        if posicion == (cont_puntos//2):
            mediana_bucle = punto
            print("Mediana:",mediana_bucle)
        posicion += 1