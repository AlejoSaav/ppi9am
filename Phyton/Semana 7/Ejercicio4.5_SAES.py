"""
Fundamentos de programación 
Sección D05

Ejercicio 4.5
Se requiere un algoritmo para obtener la estatura promedio de un grupo 
de personas, cuyo número de miembros se desconoce, el ciclo debe
efectuarse siempre y cuando se tenga una estatura registrada.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
#Declaración de variables
NumPerso=x=int()
Estatura=float()
x = 1
Suma = 0
#Entrada de datos

NumPerso=int(input("Cuantas personas son: "))

while x <= NumPerso:
    Estatura=float(input("Cual es la estatura de la persona: "))
    Suma = Suma + Estatura
    x = x + 1

print("La estatura promedio de" ,NumPerso, "personas es de: " ,Suma / NumPerso,)
