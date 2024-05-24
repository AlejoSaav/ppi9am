"""
Fundamentos de programacion D05
Ejercicio 3.14
Realice un algoritmo que, con base en una calificación proporcionada (0-10), 
indique con letra la calificación que le corresponde: 10 es
“A”, 9 es “B”, 8 es “C”, 7 y 6 son “D”, y de 5 a 0 son “F”.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaracion de variables
Calificacion=int()

#Entrada de datos
Calificacion=int(input("Cual es la calificacion asignada: "))

#Proceso
if Calificacion==10:
    print("La calificacion asignada en letra es de una A")
if Calificacion==9:
    print("La calificacion asignada en letra es de una B")
if Calificacion==8:
    print("La calificacion asignada en letra es de una C")
if Calificacion==6 or Calificacion==7:
    print("La calificacion asignada en letra es de una D")
if Calificacion<=5 or Calificacion==0:
    print("La calificacion asignada en letra es de una F")
else:
    if Calificacion<0 or Calificacion>10:
     print("Ingrese una calificacion correcta")
