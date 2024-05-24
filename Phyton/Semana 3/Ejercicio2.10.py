"""
Fundamentos de programacion D05
Ejercicio 2.10
La CONAGUA requiere determinar el pago que debe realizar una
persona por el total de metros cúbicos que consume de agua.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial
"""
#Declaración de variables
CostoMetros=CantidadAgua=PagoTotal=float()

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

CostoMetros=float(input("Cuanto vale el metro cubico: "))
CantidadAgua=float(input("Cuantos metros cubicos se gastaron: "))

#Proceso
PagoTotal=CostoMetros*CantidadAgua

#Salida de datos
print("El pago por: " ,CantidadAgua, "metros cubicos es de: ",PagoTotal, "\n")
print("Presione cualquier tecla para finalizar. . .")