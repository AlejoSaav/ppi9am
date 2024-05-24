"""
Fundamentos de programacion D05
Ejercicio 2.6
Se requiere determinar la hipotenusa de un triángulo rectángulo.


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial
"""

#Declaración de Variables
import math


aCateto=bCateto=Hipotenusa=float()

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

aCateto=float(input("Cual es la medida del cateto a: "))
bCateto=float(input("Cual es la medida del cateto b: "))

#Proceso
Hipotenusa=math.sqrt(aCateto*aCateto)+(bCateto*bCateto)

#Salida de datos
print("La medida de la hipotenusa del triangulo es de: " ,Hipotenusa, "\n")
print("Presione cualquier tecla para finalizar. . .")