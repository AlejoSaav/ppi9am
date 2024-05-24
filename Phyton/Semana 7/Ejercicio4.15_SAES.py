"""
Fundamentos de programación 
Sección D05

Ejercicio 4.15
Una empresa les paga a sus empleados con base en las horas trabajadas en
la semana. Para esto, se registran los días que laboró y las horas de cada
día. Realice un algoritmo para determinar el sueldo semanal de N trabajadores 
y además calcule cuánto pagó la empresa por los N empleados.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
#Declaracion de variables
import os
Pago=PagoHora=SueldoSemanal=float()
Horas=Dias=int()
HorasAcum=0

n = int (input ("Cuantos trabajadores son: "))
PagoHora=float(input("Cuanto se paga por hora trabajada: $"))

for can in range (1, n + 1):
    HorasTraba=0
    Dias=int(input("Cuantos dias se trabajaron: "))

    for dia in range (1, Dias + 1):
        print("\tDia" , dia)
        Horas=int(input("Cuantas horas se trabajaron: "))
        HorasTraba = HorasTraba + Horas
        print("El trabajador tiene un sueldo de $" ,HorasTraba * PagoHora,)
        HorasAcum = HorasAcum + HorasTraba

print("La empresa pago por los empleados $" ,HorasAcum * PagoHora,)


os.system ('pause')