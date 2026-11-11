"""En un estacionamiento cobran $1.500 por hora o fracción. 
Diseñe un algoritmo que determine cuánto debe pagar un cliente por el estacionamiento de su vehículo,
conociendo el tiempo de estacionamiento en horas y minutos"""

hora= float(input ("Digite las horas: "))
minutos= float(input("Digite los minutos: "))

tarifa_hora= 1500
hora_adicional = 0

if minutos < 0 or minutos >= 60: 
    print ("Digite un valor valido para los minutos")
else:
    if minutos > 0: 
        hora_adicional = 1

    horas_cobradas= hora + hora_adicional
    
    pago_total= horas_cobradas * tarifa_hora

    print (f"el pago total es de: {pago_total}")





