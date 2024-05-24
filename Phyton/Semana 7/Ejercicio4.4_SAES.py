"""
Fundamentos de programación 
Sección D05

Ejercicio 4.4
Se requiere un algoritmo para obtener la edad promedio de un grupo de N
alumnos. 

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
#Declaracion de variables
Alum=NumAlum=Edad=Suma=int()
Alum = 1
Suma=0

#Entrada de datos
NumAlum=int(input("Cuantos alumnos son: "))

#Procesos
while Alum <= NumAlum:
    Edad=int(input("Cual es la edad del alumno: "))
    Suma = Suma + Edad
    Alum += 1

#Salida de datos
print("La edad promedio de" ,NumAlum, "alumnos es de: " ,Suma / NumAlum,)