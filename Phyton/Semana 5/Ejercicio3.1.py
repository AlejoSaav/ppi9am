"""
Fundamentos de programacion D05
Ejercicio 3.1
Se desea implementar un algoritmo para determinar cual de dos valores
proporcionados es el mayor.


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""

#variables
from ast import If


Num1=Num2=Mayor=()

print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

Num1=int(input("Escribe el primer numero: ")) #Pedir al usuario el dato
Num2=int(input("Escribe el segundo numero: "))

if Num1>Num2:                                #Comparacion de datos
  Mayor=Num1                                 #Guarda el dato 
  print("El numero mayor es:" ,Mayor,)
elif Num1<Num2:                              #Vuelve a comparar el dato si el primer no resulto
  Mayor=Num2
  print("El numero mayor es:",Mayor,)
else:
  print("Es el mismo numero.")                                              


print("\n Pulse cualquier tecla para finalizar. . .")                              
                                                                
                                                                
                                                                


