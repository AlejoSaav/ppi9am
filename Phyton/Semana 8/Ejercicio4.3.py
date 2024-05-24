"""
Fundamentos de programación 
Sección D05

Ejercicio 4.3
Se requiere un algoritmo para determinar, de N cantidades, cuántas
son cero, cuántas son menores a cero, y cuántas son mayores a cero.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
import os

CantidadesCero = 0
Menores = 0
Mayores = 0
n = int (input ("Cuantos numeros desea ingresar? "))
for i in range (1, n + 1):
    print ("Numero" ,i,)
    cantidad = float (input ("Ingrese un numero: "))
    if cantidad==0:
        CantidadesCero=CantidadesCero+1
    if cantidad<0:
        Menores=Menores+1
    if cantidad>0:
        Mayores=Mayores+1
    print ()
print ("Numeros iguales a cero: " ,CantidadesCero,)
print ("Numeros menores a cero: " ,Menores,)
print ("Numeros mayores a cero: " ,Mayores,)
os.system ('pause')