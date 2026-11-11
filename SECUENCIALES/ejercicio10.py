"""Teniendo en cuenta el número de horas calcule su equivalente en minutos, segundos y días"""

horas= float(input("Digite el numero de horas: "))

minutos = horas * 60

segundos = minutos * 60

dias=horas /24

print (f"la cantidad de minutos que existen en {horas} horas es de : {minutos}")
print(f"La cantidad de segundos que existen en  {horas} horas es de {segundos}")
print(f"La cantidad de dias es de : {dias:.2f}")

