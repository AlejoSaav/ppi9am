"""
Fundamentos de programacion D05
Ejercicio 2.4
Un estacionamiento requiere determinar el cobro que debe aplicar a
las personas que lo utilizan. Considere que el cobro es con base en las
horas que lo disponen y que las fracciones de hora se toman como completas


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial
"""

#Declaración de variables
Horas=Pago=Precio=int()

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")
print("Las horas se pediran completas, no se aceptan minutos. . ." "\n")

Horas=int(input("Cuantas horas estuvo en el estacionamiento: "))
Precio=float(input("Cual es el precio por hora del estacionamiento: "))

#Proceso
Pago=Horas*Precio

#Salida de datos
print("El pago por el uso de" ,Horas, "horas es de: " ,Pago, "pesos \n")
print("Gracias por su preferencia. . .")
