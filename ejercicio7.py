# """En un estacionamiento cobran $1.500 por hora o fracción. 
# Diseñe un algoritmo que determine cuánto debe pagar un cliente por el estacionamiento de su vehículo,
# conociendo el tiempo de estacionamiento en horas y minutos"""

hora= float(input ("Digite las horas: "))
minutos= float(input("Digite los minutos: "))

valor_hora= 1500
fracion_minutos = 0

if minutos < 0 or minutos >= 60: 
    print ("Digite un valor valido para los minutos")
else:
    if minutos > 0: 
        fracion_minutos = 1
    
    valor_parqueo = hora + fracion_minutos
    pago_total= valor_parqueo * valor_hora

    print (f"el pago total es de: {valor_parqueo}")