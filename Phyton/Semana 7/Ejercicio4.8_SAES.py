"""
Fundamentos de programación 
Sección D05

Ejercicio 4.8
Realice un algoritmo para generar e imprimir los números pares que se
encuentran entre 0 y 100.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
#Declaracion de variables
x=int=()

#Procesos
x = 0
while x <= 100:
    if x % 2 == 0:
        print(x , end='\t')
    x = x + 1
