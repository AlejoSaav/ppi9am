"""
Fundamentos de programación 
Sección D05

Ejercicio 4.1
Se requiere un algoritmo para obtener la suma de diez cantidades mediante 
la utilización de un ciclo “Mientras”. 

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
#Declaración de variables
Suma=Num=Nums=float()

Suma=0
Num = 1
#Entrada de datos
print("Bienvenido al programa, sigue las indicaciones correspondientes. . .")
print("A continuacion se te pediran 10 numeros para realizar la suma de todos. . .\n")

#Procesos
while Num <= 10:
    Nums=float(input("Escribe el numero:"))
    Suma = Suma + Nums

    Num += 1

#Salida de datos
print("La suma de los 10 numeros es de: " ,Suma,)