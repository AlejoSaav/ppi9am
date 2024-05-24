import os, msvcrt, sys, __future__, statistics
import statistics
import numpy as np 
import math
def desviacionEstandar():
    lista= []
    print("Bienvenido al programa, a continuacion podras ingresar los datos a trabajar. . .")
    cantidadNum=int(input("Cuantos numeros deseas ingresar: "))
    i = 1

    while(cantidadNum>0):
     numero =float(input("Numero " + str(i) + ": "))
     lista.append(numero)
     i = i + 1
     cantidadNum = cantidadNum - 1
     

    mean = sum(lista) / len(lista)
    var = sum((l-mean)**2 for l in lista) / len(lista)
    st_dev = math.sqrt(var)
    print("La desviacion media de los datos es de: " + str(st_dev))