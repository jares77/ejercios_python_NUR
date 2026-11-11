# Una compañía de seguros está abriendo un depto. de finanzas y estableció un programa para captar clientes, que consiste en lo siguiente:
#  Si el monto por el que se efectúa la fianza es menor que $50000 la cuota a pagar será por el 3% del monto, 
# y si el monto es mayor o igual que $50000 la cuota a pagar será el 2% del monto. 
# La afianzadora desea determinar cuál será la cuota que debe pagar un cliente

fianza=float(input("Digite el monto de la fianza: "))

if fianza < 50000:
    interes = (fianza * 3) /100
else: 
    fianza >= 50000
    interes = (fianza * 2)/100

cuota= fianza + interes

print ("El interes es de: ",interes)
print ("La cuota a pagar es de: ", cuota)
