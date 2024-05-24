"""
Fundamentos de programacion D05
Ejercicio 2.8
Se requiere determinar el tiempo que tarda una persona en llegar de
una ciudad a otra en bicicleta, considerando que lleva una velocidad constante.


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial
"""
#Declaración de variables
Distancia=Velocidad=Tiempo=Horas=float()

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

Distancia=float(input("Cual es la distancia en kilometros de la siguiente ciudad: "))
Velocidad=float(input("Cual es la velocidad por kilometro a la que va: "))

#Proceso
Tiempo=(Distancia/Velocidad)*60
Horas=Tiempo/60

#Salida de datos

print("A una velocidad de" ,Velocidad, "km por hora que lleva, llegara en: " ,Horas, "Horas")

