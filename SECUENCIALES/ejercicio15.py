"""Teniendo en cuenta la cantidad de dólares que va a comprar 
y el tipo de cambio en pesos (Costo de un dólar en pesos). 
Calcular la cantidad que debe pagar en pesos por la cantidad de dólares indicada"""

cant_dolar= float(input("Digite la cantidad de dolares que desea comprar: "))
precio_dolar= float(input("Digite el precio del dolar: "))

pago_total= cant_dolar * precio_dolar

print (f"La cantidad que debe pagar es de: {pago_total} ")

