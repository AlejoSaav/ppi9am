"""
Fundamentos de programacion D05
Ejercicio 3.8
El director de una escuela está organizando un viaje de estudios, y requiere 
determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la
compañía de viajes por el servicio. La forma de cobrar es la siguiente: si
son 100 alumnos o más, el costo por cada alumno es de $65.00; de 50 a
99 alumnos, el costo es de $70.00, de 30 a 49, de $95.00, y si son menos
de 30, el costo de la renta del autobús es de $4000.00, sin importar el
número de alumnos.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaración de variables
NumAlumnos=PagoAlum=PagoTotal=int()

#Entrada de datos
NumAlumnos=int(input("Cuantos alumnos viajaran: "))


#Proceso
if NumAlumnos>=100:
    PagoAlum=65
    PagoTotal=PagoAlum*NumAlumnos
if NumAlumnos<=99 or NumAlumnos>=50:
    PagoAlum=70
    PagoTotal=PagoAlum*NumAlumnos
if NumAlumnos>=30 or NumAlumnos>=49:
    PagoAlum=95
    PagoTotal=PagoAlum*NumAlumnos
if NumAlumnos<30:
    PagoTotal=4000

#Salida de datos
print("El costo del autobus es de: ",PagoTotal,)

