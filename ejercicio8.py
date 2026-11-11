# ""Calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico; la fórmula que se aplica cuando el sexo es femenino es: num_pulsaciones = (220 − edad) /10 y si el sexo es masculino: num_pulsaciones = (210 − edad) /10""

sexo= input("Digite f para mujer y m para hombre: ").lower()
print(sexo)

edad= int(input("Digite la edad: "))
if sexo == "f":
    num_pulsaciones=  (220- edad) / 10
else:
    num_pulsaciones= (210-edad) /10

print ("El numero de pulsaciones es de : ", num_pulsaciones)
