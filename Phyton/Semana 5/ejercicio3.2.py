"""
Fundamentos de programacion D05
Ejercicio 3.1
Realice un algoritmo para determinar si un numero es positivo o negativo.
Representelo en pseudocodigo.


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaracion de variables
Num=Positivo=Negativo=int()
from ast import If
#Entrada de datos

print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

Num=int(input("Escribe el numero: "))                              


if Num<0:
    Negativo=Num
    print("El numero es negativo")
elif Num>0:
    Positivo=Num
    print("El numero es positivo")

    

