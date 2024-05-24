"""
Fundamentos de programacion D05
Ejercicio 3.5
Se requiere determinar cuál de tres cantidades proporcionadas es la
mayor.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaración de variables
Num1=Num2=Num3=int()
import os

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

Num1=int(input("Ingrese el primer numero: "))
Num2=int(input("Ingrese el segundo numero: "))
Num3=int(input("Ingrese el tercer numero: "))

#Proceso
if Num1>Num2 and Num1>Num3:
    print("El numero mayor es: ",Num1,)
elif Num2>Num1 and Num2>Num3:
    print("El numero mayor es: ",Num2,)
elif Num3>Num1 and Num3>Num2:
    print("El numero mayor es: ",Num3,)

#salida de datos
os.system('pause')

