lista_puntos = [4, 5, 6, 8, 10, 20, 30, 40, 50, 60]
cont_puntos = 0
posicion = 0
for punto in lista_puntos:
    cont_puntos = cont_puntos + 1
for punto in lista_puntos:
    if posicion == (cont_puntos//2):
        print(punto)
    posicion += 1