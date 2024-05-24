"""
Fundamentos de programacion D05

Ejercicio 2.10
La conagua requiere determinar el pago que debe realizar una persona 
por el total de metros cúbicos que consume de agua al llenar una alberca. 
Realizar el algoritmo correspondiente para resolver este problema.  


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
#Declaración de variables
Altura=Largo=Ancho=CostoMetro=Volumen=Pago=float()

#Entrada de datos
Altura=float(input("Cual es la altura de la alberca?: "))
Largo=float(input("Cual es el largo de la alberca?: "))
Ancho=float(input("Cual es el ancho de la alberca?: "))
CostoMetro=float(input("Cuanto es el costo del metro cubico?: "))

#Proceso
Volumen=Altura*Largo*Ancho
Pago=Volumen*CostoMetro

#Salida de datos
print("El pago a realizar por la alberca es de: " ,Pago, "\n")
print("Presione cualquier tecla para finalizar. . .")