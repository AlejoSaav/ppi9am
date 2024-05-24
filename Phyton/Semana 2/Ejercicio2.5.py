"""
Fundamentos de programacion D05
Ejercicio 2.5
Una empresa desea conocer el área de un terrero que esta por vender, 
realizar un algoritmo que solicite las medidas de cada 
lado del terrero y haga el proceso correspondiente para sacar el área solicitada

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
#Declaración de variables
A=B=C=AT=AR=Area=Resta=float()

#Entrada de datos
A=float(input("Escribe la altura del lado A: "))
B=float(input("Escribe la base del lado B: "))
C=float(input("Escribe la altura del lado C: "))

#Proceso
Resta=A-C
AT=(B*Resta)/2
AR=B*Resta
Area=AT+AR

#Datos de salida
print("El area del terreno es de: " ,Area, "\n")
print("Pulse cualquier tecla para finalizar. . .")
