"""
Fundamentos de programación 
Sección D05

Ejercicio 4.5
Se requiere un algoritmo para determinar cuánto ahorrará en pesos
una persona diariamente, y en un año, si ahorra 3¢ el primero de
enero, 9¢ el dos de enero, 27¢ el 3 de enero y así sucesivamente
todo el año.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
import os
import math

ahorroAnual = 0
for i in range (1, 366):
    print ("Dia" ,i,)
    ahorroAnual=ahorroAnual+0.01*math.pow(3,i)
    ahorroDiario=ahorroAnual
    print ("Dinero ahorrado diario $ ",ahorroDiario,)
    os.system('pause')
    os.system('cls')
print ("Dinero ahorrado durante el año $",ahorroAnual,)
os.system ('pause')