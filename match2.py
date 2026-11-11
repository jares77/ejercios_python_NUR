#and significa que ambas condiciones deben cumplirse.
#or significa que basta con que una condición se cumpla.

print("1.Suma\n2.Resta\n3.Multiplicación\n4.División")
resultado = 0
opcion = int(input("Digite la opción "))
if opcion <= 0 or opcion > 4:
    print("Opción incorrecta")
else:
    numero1 = int(input("Digite un número 1:  "))
    numero2 = int(input("Digite un número 2:  "))

    match opcion:

        case 1:
            resultado = numero1 + numero2

        case 2:
            resultado = numero1 - numero2

        case 3:
            resultado = numero1 * numero2

        case 4:
            if numero2 == 0:
                print("No se puede dividir entre cero")
            else:
                resultado = numero1 / numero2
        case _:
            pass
              
    if opcion != 4 or numero2 != 0:
         print(f"El resultado es: {resultado:,.0f}")