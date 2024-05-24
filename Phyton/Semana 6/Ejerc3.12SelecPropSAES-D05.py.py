"""
Fundamentos de programacion D05
Ejercicio 3.12 
Realice un algoritmo que permita determinar el sueldo semanal de un trabajador con base 
en las horas trabajadas y el pago por hora, considerando que a partir de la hora número 41 y hasta 
la 45, cada hora se le paga el doble, de la hora 46 a la 50, el triple, 
y que trabajar más de 50 horas no está permitido.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaracion de variables 
Horas=Pago=Sueldo=int()

#Entrada de datos
Horas=int(input("Cuantas horas se trabajaron: "))
Pago=float(input("Cuanto se paga por hora: "))

#Proceso
Sueldo=Horas*Pago
if Horas>40:
    Sueldo=Horas*Pago+(Horas-40)*Pago
if Horas>46:
    Sueldo=Horas*Pago+(Horas-45)*Pago
if Horas>50:
    Sueldo=0
    print("No se puede trabajar mas de 50 horas. . .")

#Salida de datos
print("Por las",Horas,"hora(s) trabajas el sueldo es de $",Sueldo,)
    