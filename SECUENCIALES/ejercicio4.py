"""Factura de restaurante: subtotal, IVA y propina.  Enunciado: En un restaurante, una familia
ordena varios platos. El mesero informa el subtotal antes de impuestos. En tu ciudad, 
el IVA se cobra como un porcentaje del subtotal. Además, la familia desea dejar una propina,
también expresada como porcentaje del subtotal. Se te pide calcular el total a pagar 
(subtotal + IVA + propina). No hay cargos adicionales ni descuentos. Datos a ingresar:
• Subtotal de la cuenta (en dinero) • Porcentaje de IVA (por ejemplo, 19 para 19%) 
• Porcentaje de propina (por ejemplo, 10 para 10%) Pistas de resolución (secuenciales):
Calcular IVA = subtotal * (ivaPorc/100). - Calcular propina = subtotal * (propinaPorc/100). - Total = subtotal + IVA + propina."""

print("((((FACTURA DE RESTAURANTE))))")

subtotal= int(input("Digite el subtotal de la compra: "))
iva= int(input("Digite el IVA correspondiente: "))
propina= int(input("Digite el porcentage en propina que desea el cliente: "))

iva= subtotal * (iva/100)
propina= subtotal * (propina/100)
total_pagar= subtotal + iva + propina
print ("El iva corresponde a: ", iva)
print ("la propina corresponde a : ", propina)
print("El total a pagar corrersponde a : ", total_pagar)