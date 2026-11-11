"""Calcular el salario que debe recibir una persona teniendo en cuenta lo siguiente, 
el salario básico mensual se ingresa por teclado, el número de horas extras se ingresa por teclado,
el tipo de horas extras que puede trabajar la persona son; horas extras diurna,
el valor de una hora extra diurna corresponde a 25% más del valor de la hora normal de trabajo,
horas extras nocturnas el valor de una hora extra nocturna corresponde a 35% más del valor de la hora normal de trabajo,
horas extras festivas el valor de una hora extra festiva corresponde a 75% más del valor de la hora normal de trabajo,
horas extras dominicales el valor de una hora extra dominica corresponde a 100% más del valor de la hora normal de trabajo.
El número de horas extras que trabaja la persona se ingresan por teclado. Al trabajador le descuenta del total de 
lo que recibe el 4% para salud y el 4% para pensión. Se debe tener presente que el trabajador puede fallar uno o más
días y si es así se debe descontar ese día(s) del salario básico. El algoritmo debe mostrar salario básico, 
total de ingresos por horas extras, descuentos y total a pagar. (Para calcular el día se debe dividir
el salario básico en 30 y el valor de una hora es igual al día dividió en 8 horas diarias)."""

salario_basic_mensual= float(input("Digite el salario basico del empleado: "))
sueldo_dia= salario_basic_mensual/30
hora=sueldo_dia/8       

#calculo hora extra diurna:
horas_ext_diurnas= float(input("Digite las horas extras diurnas del empleado: "))#25% mas del valor de la hora normal
porcen_hora_diurna=(hora*25)/100

total_hora_diurna_mas_porcentage = hora + porcen_hora_diurna 
valor_total_extras_diurnas = total_hora_diurna_mas_porcentage * horas_ext_diurnas

# calculo hora extra nocturna:
horas_ext_nocturna= float(input("Digite las horas extras nocturnas del empleado: "))#35% mas del valor de la hora normal
porcen_hora_nocturna=(hora*35)/100

total_hora_nocturna_mas_porcentage = hora + porcen_hora_nocturna 
valor_total_extras_nocturna = total_hora_nocturna_mas_porcentage * horas_ext_nocturna

# calculo hora extra festiva:
horas_ext_festiva= float(input("Digite las horas extras festivas del empleado: "))#75% mas del valor de la hora normal
porcen_hora_festiva=(hora*75)/100

total_hora_festiva_mas_porcentage = hora + porcen_hora_festiva 
valor_total_extras_festivas = total_hora_festiva_mas_porcentage * horas_ext_festiva

#calculo horas extras dominicales:
horas_ext_dominicales= float(input("Digite las horas extras dominicales del empleado: "))#100% mas del valor de la hora normal
porcen_hora_dominicales = hora 

total_hora_dominical_mas_porcentage = hora * 2 
valor_total_extras_dominicales = total_hora_dominical_mas_porcentage * horas_ext_dominicales

#calculo dias ausentes: 
dias_faltantes= float(input("Digite los dias de falla del empleado: ")) #descontar el dia del salario basico"""
valor_descue_fallas =  sueldo_dia * dias_faltantes


#descuento por salud y pension:
desc_salud=  (salario_basic_mensual*4)/100
desc_pension = (salario_basic_mensual*4)/100

#calculo total de ingresos: 
total_ingre_horas_extras = valor_total_extras_diurnas + valor_total_extras_nocturna + valor_total_extras_festivas + valor_total_extras_dominicales

#calculo total descuentos: 
total_descuentos = valor_descue_fallas + desc_salud + desc_pension
#neto a pagar= 

sueldo_neto = (salario_basic_mensual + total_ingre_horas_extras) - total_descuentos 
print("*******************************************************************************")

print ("el salario basico es de : ", round (salario_basic_mensual,2))
print ("el sueldo del dia es de : ", round (sueldo_dia,2))
print ("la hora equivale a: ", round (hora,2))
print("*******************************************************************************")

print("el valor adicional de las horas diurna es de: ", round (porcen_hora_diurna,2))
print("el nuevo valor de la hora diurna es de: ", round (total_hora_diurna_mas_porcentage,2))
print ("el valor de las horas extras diurnas es de: ", round (valor_total_extras_diurnas,2))
print("*******************************************************************************")

print("el valor adicional de las horas nocturna es de: ", round (porcen_hora_nocturna,2))
print("el nuevo valor de la hora nocturna es de: ", round (total_hora_nocturna_mas_porcentage,2))
print ("el valor de las horas extras nocturna es de: ", round (valor_total_extras_nocturna,2))
print("*******************************************************************************")

print("el valor adicional de las horas festivas es de: ", round (porcen_hora_festiva,2))
print("el nuevo valor de la hora festivas es de: ", round (total_hora_festiva_mas_porcentage,2))
print ("el valor de las horas extras festivas es de: ", round (valor_total_extras_festivas,2))
print("*******************************************************************************")

print("el valor adicional de las horas dominicales es de: ", round (porcen_hora_dominicales,2))
print("el nuevo valor de la hora dominicales es de: ", round (total_hora_dominical_mas_porcentage,2))
print ("el valor de las horas extras dominicales es de: ", round (valor_total_extras_dominicales,2))
print("*******************************************************************************")

print("el valor de los dias faltantes es de: ", round(valor_descue_fallas,2))
print("*******************************************************************************")

print ("el descuento de salud es de: ", round(desc_salud,2))
print ("el descuento de pension es de: ", round(desc_pension,2))
print("*******************************************************************************")

print("el total de los descuentos fue de: ", round(total_descuentos,2))
print ("el neto a pagar es de: ",round(sueldo_neto,2))

