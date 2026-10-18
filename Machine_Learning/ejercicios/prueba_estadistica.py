notas = [5, 9, 8, 6, 4, 10, 8, 4.5, 7, 6]
nota_mas_alta = notas[0]
nota_mas_baja = notas[0]
posicion = 0
for nota in notas:
    print(nota)
    if nota > nota_mas_alta:
        nota_mas_alta = nota
    if nota < nota_mas_baja:
        nota_mas_baja = nota
print("Nota más alta:", nota_mas_alta)
print("Nota más baja:", nota_mas_baja)