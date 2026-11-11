"""Calcular el total que una persona debe pagar en una llantera,
si el precio de cada llanta es de $800 si se compran menos de 5 llantas
y de $700 si se compran 5 o más."""

cant_llantas= int(input("Digite la cantidad de llantas compradas: "))

if cant_llantas >= 5: #el (if) remplaza el romboy en pseint
    precio = 700
else:
    precio = 800 

total= precio * cant_llantas

print (f"el total a pagar es de : {total}")
