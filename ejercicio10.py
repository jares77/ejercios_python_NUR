"""Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario. Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena. Diseñe un algoritmo que determine el monto de la compra, el monto del descuento, el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de docenas del producto"""

precio= int(input("Digite el precio del producto: "))
docenas= int(input("Digite las docenas compradas: "))

monto_compra = precio * docenas

if docenas > 3:
    descuento = (monto_compra * 15)/100
    obsequio= docenas
        
else:
        descuento = (monto_compra * 10)/100
        obsequio=0
monto_pagar = monto_compra - descuento

print ("El precio total de la compra es de: ",monto_compra)
print ("El descuento de la compra es de: ",descuento)
print ("El monto total es de: ",monto_pagar)
print ("El cliente recibe " ,obsequio, "unidades")




