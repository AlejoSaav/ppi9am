"""
Fundamentos de programación 
Sección D05

Ejercicio 4.14
Realice un algoritmo para leer las calificaciones de N alumnos y de-
termine el número de aprobados y reprobados.


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
import os

aprobados = 0
reprobados = 0
calificacionAprobatoria = float (input ("Cual es la calificacion aprobatoria: "))
n = int (input ("Ingresa la cantidad de alumnos: "))
for i in range (1, n + 1):
    print ("Alumno " ,i,)
    calificacion = float (input ("Cual es la calificacion: "))
    if calificacion>=calificacionAprobatoria:
        aprobados=aprobados+1
    else:
        reprobados=reprobados+1
    
print ("Aprobados: " ,aprobados,)
print ("Reprobados: " ,reprobados,)
os.system ('pause')