print("1.Suma\n2.Resta\n3.Multiplicación\n4.División")
#12

y=0
x=1 
opcion=int(input("Digite la opción "))
if opcion <=0 or opcion >4 :
    print("Digite una opcion valida")
    x=0
if x!=0:    
    numero1 =int(input("Digite un número "))
    5
    numero2 =int(input("Digite un número "))
    resultado = False
    #       12
    match opcion:

        case 1:
            resultado = numero1 + numero2

        case 2:
            resultado = numero1 -  numero2
        case 3:
            #15
            resultado =  numero1 * numero2
        case 4:
            if numero2==0 :
              y=1
              
            else :
                resultado = numero1 / numero2
            
        case _:
            pass
        


    if y== 0 :
        if resultado == False:
            print("No seleciona una opción valida")
        else:

            print(f"El resultado es {resultado:,.1f}")
    else :
        print("Resultado infinito4")