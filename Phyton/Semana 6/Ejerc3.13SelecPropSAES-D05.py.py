"""
Fundamentos de programacion D05
Ejercicio 3.13
Los alumnos de una escuela desean realizar un viaje de estudios,
pero requieren determinar cuánto les costará el pasaje, considerando que 
las tarifas del autobús son las siguientes: si son más de 100 alumnos, 
el costo es de $20; si son entre 50 y 100, $35; entre 20 y 49, $40, y si 
son menos de 20 alumnos, $70 por cada uno. 

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaración de variables
NumAlumnos=PagoTotal=int()

#Entrada de datos
NumAlumnos=int(input("Cuantos alumnos iran en autobus: "))

if NumAlumnos<20:
    PagoTotal=NumAlumnos*70
if NumAlumnos>=20 and NumAlumnos<=49:
    PagoTotal=NumAlumnos*40
if NumAlumnos>=50 and NumAlumnos<=100:
    PagoTotal=NumAlumnos*35
if NumAlumnos>100:
    PagoTotal=NumAlumnos*20

#Salida de datos
print("Por",NumAlumnos, "alumnos, se pagara la cantidad de $",PagoTotal,)
