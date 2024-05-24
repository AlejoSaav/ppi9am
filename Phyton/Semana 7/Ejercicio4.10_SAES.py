"""
Fundamentos de programación 
Sección D05

Ejercicio 4.10
Una empresa tiene el registro de las horas que trabaja diariamente un
empleado durante la semana (seis días) y requiere determinar el total de
éstas, así como el sueldo que recibirá por las horas trabajadas.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""

#Variables
x=Horas=int()
Pago=Sueldo=Total=float()
Horas = 0
Sueldo = 0

#Entrada de datos
Pago=float(input("Cuanto se paga por hora: $"))
for i in range (1, 7):
    print("Dia" ,i)
    Horas=int(input("Cuantas horas se trabajaron: "))
    Total = Total + Horas
Sueldo = Pago * Total
print ("Total de horas que se trabajaron fueron: ",Total,)
print ("El sueldo es de $",Sueldo,)
