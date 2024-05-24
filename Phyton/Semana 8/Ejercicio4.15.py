"""
Fundamentos de programación 
Sección D05

Ejercicio 4.15
Realice un algoritmo que determine el sueldo semanal de N trabajadores 
considerando que se les descuenta 5% de su sueldo si ganan
entre 0 y 150 pesos. Se les descuenta 7% si ganan más de 150 pero
menos de 300, y 9% si ganan más de 300 pero menos de 450. Los
datos son horas trabajadas, sueldo por hora y nombre de cada trabajador.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
import os

n = int (input ("Cuantos trabajadores son? "))
for i in range (1, n + 1):
    print ("Trabajador " ,i,)
    nombreTrabajador = (input ("Nombre del trabajador: "))
    horasTrabajadas = float (input ("Horas trabajadas: "))
    sueldoHora = float (input ("Sueldo por hora: "))
    sueldoSemanal=horasTrabajadas*sueldoHora
    descuento=0
    if sueldoSemanal>0 and sueldoSemanal<=150:
        descuento=sueldoSemanal*0.05
    if sueldoSemanal>150 and sueldoSemanal<=300:
        descuento=sueldoSemanal*0.07
    if sueldoSemanal>300 and sueldoSemanal<=450:
        descuento=sueldoSemanal*0.09
    sueldoSemanal=sueldoSemanal-descuento
    print ("\nNombre del trabajador: " ,nombreTrabajador,)
    print ("Descuento: " ,descuento,)
    print ("Sueldo semanal: " ,sueldoSemanal,)
    os.system('pause') 
 
