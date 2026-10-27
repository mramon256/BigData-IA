inventario = {
 "ratón": 12,
 "teclado": 5,
 "monitor": 0,
 "cable": 25
}

total = 0
for producto, cantidad in inventario.items():
    total += cantidad
    if cantidad < 10:
        print(producto)
print(total)