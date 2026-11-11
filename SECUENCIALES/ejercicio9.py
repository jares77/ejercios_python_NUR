"""Calcular el costo de un terreno cuadrado o rectangular, teniendo como datos la anchura y el largo en metros y el costo del metro cuadrado"""

costo_metro_cuadr= float(input("Digite el costo del metro cuadrado: "))
ancho=  float(input("Digite el ancho del terreno en metros: "))
largo=  float(input("Digite el largo del terreno en metros: "))

area= ancho * largo
costo_total = area * costo_metro_cuadr

print("*********************************************")
print(f"El area del terreno es de: {area}")
print (f"El precio total del terreno es de {costo_total}")
