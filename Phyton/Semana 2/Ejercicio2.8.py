"""
Fundamentos de programacion D05

Ejercicio 2.8
Se requiere obtener la distancia entre dos puntos en el plano cartesiano. 
Realizar un algoritmo para resolver este problema. 

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
import math

#Declaración de variables
X1=X2=Y1=Y2=X=Y=Distancia=float()

#Entrada de datos
X1=float(input("Escribe la posicion de X1: "))
Y1=float(input("Escribe la posicion de Y1: "))

X2=float(input("Escribe la posicion de X2: "))
Y2=float(input("Escribe la posicion de Y2: "))

#Proceso
X=X2-X1
Y=Y2-Y1
Distancia=(math.sqrt(X*X+Y*Y))

#Salida de datos
print("La distancia de los puntos es de:" ,Distancia, "\n")
print("Pulse cualquier tecla para finalizar. . .")