"""
Fundamentos de programación 
Sección D05

Ejercicio 4.10
Los directivos de equis escuela requieren determinar cuál es la edad
promedio de cada uno de los M salones y cuál es la edad promedio de toda la escuela. 

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
import os
#Variables
x=CanAlum=salones=alumnos=edad=suma=total=int()

#Entrada de datos

salones=int(input("Cuantos salones son? "))

while salones > 0:
    CanAlum=int(input("Cuantos alumnos son? "))
    suma=0
    for x in range (1, CanAlum + 1):
        edad=int(input("Cual es la edad del alumno? " ))
        suma=suma+edad
        print("El promedio del salon ",salones, "es de: ",suma/CanAlum, "años")
        alumnos = alumnos + CanAlum
        total = total + suma
        salones = salones - 1
print("El promedio de toda la escuela es: " ,total/alumnos, " años")
os.system('pause')