"""
Fundamentos de programacion D05
Ejercicio 2.3
Una empresa que contrata personal requiere determinar la edad de
las personas que solicitan trabajo, pero cuando se les realiza la entrevista 
sólo se les pregunta el año en que nacieron.


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
#Declaración de variables
Año=Edad=int()
from datetime import date

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")
Año=int(input("Cual es el año de nacimiento de la persona: "))

#Proceso
Edad=date.today().year-Año

#Salida de datos
print("La edad de la persona es de: " ,Edad, "años \n")
print("Pulse cualquier tecla para finalizar. . .")
