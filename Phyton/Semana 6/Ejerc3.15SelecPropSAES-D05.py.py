"""
Fundamentos de programacion D05
Ejercicio 3.15
Realice un algoritmo que, con base en un número proporcionado
(1-7), indique el día de la semana que le corresponde

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaracion de variables
NumSemana=int()

#Entrada de datos
NumSemana=int(input("Ingrese un numero del 1 al 7: "))

#Proceso
if NumSemana==1:
    print("El numero corresponde al dia de la semana Lunes")
if NumSemana==2:
    print("El numero corresponde al dia de la semana Martes")
if NumSemana==3:
    print("El numero corresponde al dia de la semana Miercoles")
if NumSemana==4:
    print("El numero corresponde al dia de la semana Jueves")
if NumSemana==5:
    print("El numero corresponde al dia de la semana Viernes")
if NumSemana==6:
    print("El numero corresponde al dia de la semana Sabado")
if NumSemana==7:
    print("El numero corresponde al dia de la semana Domingo")
elif NumSemana>7:
    print("El numero no corresponde a ningun dia de la semana")


