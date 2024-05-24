"""
Fundamentos de programación 
Sección D05

Ejercicio 4.11
Realice un algoritmo y represéntelo mediante un diagrama de flujo
para obtener una función exponencial, la cual está dada por:


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
n=a=int()
x=e=f=float()

import os, math

ex = 0
factorial = 0
n = int (input ("Numero de repeticiones: "))
x = float (input ("Ingresa el valor de x: "))

for i in range (1, n + 1):
    print ("Repeticion " ,i,)
    if i==1:
        ex=1
        factorial=1
    factorial=factorial*i
    ex=ex+math.pow(x,i)/factorial
    print ()
print ("Valor de ex: " ,ex,)
print ("Valor de factorial: " ,factorial,)
os.system ('pause')
