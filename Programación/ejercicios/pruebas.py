productos = ["pan", "leche", "arroz", "huevos"]
precios = [1.20, 0.95, 2.10, 2.80]
total = 0

for producto, precio in zip(productos, precios):
    total += precio
    print(producto, precio)
    print(total)