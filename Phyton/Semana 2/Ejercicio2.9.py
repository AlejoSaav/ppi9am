"""
Fundamentos de programacion D05

Ejercicio 2.9
Se desea determinar el sueldo semanal de un trabajador con base en las horas que trabaja 
y el pago por hora que recibe. Realizar un algoritmo para solucionar este problema. 

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""

#Declaración de variables
Horas=Pago=PagoSemanal=float()

#Entrada de datos
Horas=float(input("Cuantas horas se trabajaron?: "))
Pago=float(input("Cual es el pago por hora?:"))

#Proceso
PagoSemanal=Horas*Pago

#Salida de datos
print("El sueldo de esta semana es de: " ,PagoSemanal, "\n")
print("Pulse cualquier tecla para finalizar. . .")