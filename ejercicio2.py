"""Ingresar el nombre de un empleado, las horas trabajadas, luego Calcular pago bruto
$8.000 pesos por hora trabajada y total a pagar, presentar los resultados del programa.
Nota: el seguro social es de 8.5% del total de lo que recibe si el sueldo es mayor 800 dólares,
sino es el 3.5% del sueldo del empleado.
"""
nombre= input("ingrese el nombre del empleado: ")
horas_trabajo = int(input("Ingrese las horas trabajadas: "))
valor_hora= 8000
pago_bruto = horas_trabajo * valor_hora
dolar= 4000
limite_dolar= 800 * dolar #3200 dolares

if pago_bruto > limite_dolar:
    seguro_social = (pago_bruto * 8.5)/100  
else:
    seguro_social = (pago_bruto * 3.5)/100

total_pagar = pago_bruto - seguro_social

print("el nombre del empleado es: ", nombre)
print ("el pago bruto es: ", pago_bruto)
print("el seguro social es de: ", seguro_social)
print ("el neto a pagar es de: ", total_pagar)




