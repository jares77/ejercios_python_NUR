"""enunciado: Una tienda anuncia un descuento sobre el precio de lista de un televisor.
Después de aplicar el descuento, se debe sumar el impuesto nacional 
y el impuesto municipal (ambos como porcentajes), calculados sobre 
el precio ya descontado. Calcule el precio final al comprador."""

precio_tv= int(input("Digite el nuevo precio del TV: "))
imp_nacional= float(input("Digite el impuesto nacional: "))
imp_municipal= float(input("Digite el impuesto municipal: "))

imp_nacional= (precio_tv * imp_nacional)/100
imp_municipal= (precio_tv * imp_municipal)/100

precio_total= precio_tv + imp_municipal + imp_nacional

print(f"El precio total del tv es de : {precio_total}")
print("_"*50)

#2da forma de hacerlo:

precio_tv= int(input("Digite el precio del tv: "))
porc_descuento= float(input("Digite el porcentage de descuento: "))
porc_descuento = (precio_tv * porc_descuento)/100
nuevo_precio= precio_tv - porc_descuento

print (f"El descuento es de : {porc_descuento}")
print(f"El nuevo precio es de : {nuevo_precio}")

imp_nacional=int(input("Digite el impuesto nacional: "))
imp_municipal= int(input("Digite el impuesto municipal: "))
imp_nacional= (nuevo_precio * imp_nacional) /100
imp_municipal = (nuevo_precio * imp_municipal) /100
precio_total = nuevo_precio + imp_nacional + imp_municipal
print (f"El nuevo precio del tv es de {precio_total}")