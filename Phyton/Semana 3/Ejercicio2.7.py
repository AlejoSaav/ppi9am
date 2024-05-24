"""
Fundamentos de programacion D05
Ejercicio 2.6
La compañía de autobuses “La curva loca” requiere determinar el costo 
que tendrá el boleto de un viaje sencillo, esto basado en los kilómetros 
por recorrer y en el costo por kilómetro.


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial
"""
#Declaración de variables 
KilometrosReco=PrecioKilometro=PagoTotal=float()

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

PrecioKilometro=float(input("Cual es el precio por kilometro recorrido: "))
KilometrosReco=float(input("Cuantos kilometros va recorrer: "))

#Proceso
PagoTotal=PrecioKilometro*KilometrosReco

#Salida de datos
print("El precio por recorrer:" ,KilometrosReco, "es de:" ,PagoTotal, "pesos \n")
print("Presione cualquier tecla para finalizar. . .")

