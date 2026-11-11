"""Calcular la calificación final de un estudiante. Los datos disponibles para lectura son calificación 1, 
equivale al 30% de la nota final, calificacion2, equivale al 20% de la nota final, calificacion3,
equivale al 10% de la nota final, calificacion4, equivale al 40% de la nota final
de cada uno de los cuatro exámenes presentados. La información que se debe imprimir 
es el promedio de las calificaciones."""

calificacio1= float(input("Ingrese la nota uno del estudiante: "))
calificacion2= float(input("Ingrese la nota dos del estudiante: "))
calificacion3= float(input("Ingrese la nota tres del estudiante: "))
calificacion4= float(input("Ingrese la nota cuatro del estudiante: "))
promedio= (calificacio1+calificacion2+calificacion3+calificacion4)/4

nota1= (promedio * 30)/100
nota2= (promedio *20)/100
nota3= (promedio *10)/100
nota4= (promedio *40)/100
nota_final= (nota1+nota2+nota3+nota4)

print("************************************************")

print(f"El promedio de la calificacion 1 es de  : {nota1}")
print(f"El promedio de la calificacion 2 es de  : {nota2}")
print(f"El promedio de la calificacion 3 es de  : {nota3}")
print(f"El promedio de la calificacion 4 es de  : {nota4}")
print(f"La nota fina es de : {nota_final:.2f}") 