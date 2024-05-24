"""
Fundamentos de programacion D05
Ejercicio 2.8
Se requiere determinar el costo que tendrá realizar una llamada telefónica
con base en el tiempo que dura la llamada y en el costo por minuto.


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial
"""

#Declaración de variables
TiempoLlamada=CostoMinuto=Pago=float()

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

TiempoLlamada=float(input("Cuantos minutos duro la llamada: "))
CostoMinuto=float(input("Cuanto cuesta el minuto de llamada: "))

#Proceso
Pago=TiempoLlamada*CostoMinuto

#Salida de datos
print("El costo por:",TiempoLlamada, "min es de: " ,Pago, "\n" )
print("Pulse cualquier tecla para salir. . .")
