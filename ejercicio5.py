"""Construir un algoritmo tal, que dado como dato la calificación de un alumno en un examen,
escriba "Aprobado" en caso de que esa calificación fuese mayor que 8. 
Un alumno aprueba si la calificación es mayor que 8
NOTA: la calificacio no puede ser menos a (0) y mayor a 10, en caso de digitarse los 
numeros en este rango el programa debe mostrar: "CALIFICACION INVALIDA" """

calificacion= float (input("Digite la calificacion del alumno:"))
if calificacion < 0 or calificacion > 10:
    print ("CALIFICACION INVALIDA")
elif calificacion > 8: #elif traduce: ("sino y resulta que...")
    print ("Aprobado")
else:
    print("No aprobado")
print("Trabajando python")
