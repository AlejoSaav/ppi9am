"""
Fundamentos de programación 
Sección D05

Ejercicio 4.6
Se requiere un algoritmo para determinar cuánto ahorrará una persona
en un año, si al final de cada mes deposita variables cantidades de dinero; 
además, se requiere saber cuánto lleva ahorrado cada mes.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
#Declaracion de variables
import os
Ahorro=Suma=float()
x = 1
Suma = 0

#Entrada de datos

#Proceso
while x <= 12:
    Ahorro=float(input("Ingrese la cantidad de ahorro de este mes: "))
    Suma = Suma + Ahorro
    print("El ahorro acumulado hasta el mes de ",x, "es de $" ,Suma,)
    os.system('pause')
    os.system('cls')
    x = x + 1

print("El ahorro total del año es de $",Suma,)