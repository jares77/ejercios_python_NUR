"""Calcular el precio de venta de un artículo, se tienen los datos de descripción del artículo el costo de producción.
El precio de venta se calcula añadiendo al costo el 120% como utilidad y el 15%de impuesto"""

nombre_articulo=input("Ingrese el nombre del articulo: ")
costo_produccion= float(input("Ingrese el costo de produccion del articulo: "))
utilidad= (costo_produccion * 120) /100
impuesto= (costo_produccion * 15)/100
precio_venta= utilidad + impuesto + costo_produccion

print (f"El precio fina del articulo es de : {precio_venta}")

