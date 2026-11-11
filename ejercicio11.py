"""Una persona enferma, que pesa 70 kg, se encuentra en reposo y desea saber 
cuántas calorías consume su cuerpo durante todo el tiempo que realice una misma actividad. 
Las actividades que tiene permitido realizar son únicamente dormir o estar sentado en reposo. 
Los datos que tiene son que estando dormido consume 1.08 calorías por minuto y 
estando sentado en reposo consume 1.66 calorías por minuto"""

actividad= input("Ingrese la actividad a realizar: ")
tiempo_actividad= float(input("Ingrese el tiempo de la actividad: "))

consumo_por_minuto= 0

calorias_dormir=1.08
calorias_sentado= 1.66


calorias = tiempo_actividad * consumo_por_minuto

if actividad == calorias_dormir: 
    calorias = tiempo_actividad *  calorias_dormir
else : 
    calorias = tiempo_actividad *  calorias_sentado
    
print ("las calorias consumidas fueron de: ", calorias)

