"""
Fundamentos de programacion D05
Ejercicio 2.2
Un estudiante realiza 4 exámenes durante un semestre, se requiere un algoritmo 
que pida al usuario ingresar 4 números y que este de un promedio como resultado.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial


"""
#Declaración de variables
C1=C2=C3=C4=Suma=Prom=float()

#Entrada de datos 
C1=float(input("Escribre la primera calificacion:"))
C2=float(input("Escribe la segunda calificacion:"))
C3=float(input("Escribe la tercera calificacion:"))
C4=float(input("Escribe la cuarta calificacion:"))

#Procesos
Suma=C1+C2+C3+C4
Prom=Suma/4

print("Tu promedio es:" ,Prom, "\n")

print("Presione cualquier tecla para finalizar")
