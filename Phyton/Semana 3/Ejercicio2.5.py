"""
Fundamentos de programacion D05
Ejercicio 2.5
Pinturas “La brocha gorda” requiere determinar cuánto cobrar por
trabajos de pintura. Considere que se cobra por m2


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial
"""
#Declaración de variables
MetrosCuadrados=PrecioMetros=Pago=float()

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

PrecioMetros=float(input("Cual es el precio por metro cuadrado: "))
MetrosCuadrados=float(input("Cuantos metros cuadrados se van a trabajar: "))

#Proceso
Pago=PrecioMetros*MetrosCuadrados

#Salida de datos
print("El pago por pintar" ,MetrosCuadrados, "m2 es de: " ,Pago, "pesos \n")
print("Gracias por su preferencia. . .")
