"""Calcular el costo de un artículo. La utilidad es de 150% y el impuesto es el 15%.
Calcule e imprima Utilidad, impuesto y precio de venta"""

costo_produccion= float(input("Digite el costo de produccion del articulo: "))
utilidad= float(input("Digite el porcentage de utilidad del articulo: "))
impuesto= float(input("Digite el impuesto del articulo: "))

utilidad = (costo_produccion * 150) /100
impuesto = (costo_produccion * 15)/ 100

precio_venta= costo_produccion + utilidad +impuesto

print ("La utilidad es de: ", utilidad)
print ("El impuesto es de: ", impuesto)
print ("El precio de venta es de: ", precio_venta)

