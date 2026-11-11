"""Calcular el promedio de calificación de un estudiante. Los datos disponibles para lectura son calificación1, calificacion2, calificacion3, calificacion4 de cada uno de los cuatro exámenes presentados. La información que se debe imprimir es el promedio de las calificaciones"""
nota1=float(input("Ingrese la nota uno del estudiante: "))
nota2=float(input("Ingrese la nota dos del estudiante: "))
nota3=float(input("Ingrese la nota tres del estudiante: "))
nota4=float(input("Ingrese la nota cuatro del estudiante: "))

promedio= (nota1+nota2+nota3+ nota4)/4

print (f"El promedio del estudiante es de : {promedio:.2f}")