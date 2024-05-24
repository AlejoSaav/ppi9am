import os, msvcrt, sys, __future__, statistics
import statistics
import numpy as np 
import math

def media():
    lista= []
    print("Bienvenido al programa, a continuacion podras ingresar los datos para sacar la media. . .")
    cantidadNum=int(input("Cuantos numeros deseas ingresar: "))
    i = 1

    while(cantidadNum>0):
     numero =float(input("Numero " + str(i) + ": "))
     lista.append(numero)
     i = i + 1
     cantidadNum = cantidadNum - 1
     
    promedio = sum(lista)/len(lista)

    print("El promedio es de: ",promedio,)