"""

Materia: Fundamentos de programacion Seccion D05
Carrera: Ingenieria en computación
Alumno: Elisea Saavedra Samuel Alejandro
Tema: Estructura de control selectivda anidada
Maestro: Conrado Cruz Gomez 

Ejercicio 4.-
Realiza un programa que reciba un año e imprima "EL AÑO ES BISIESTO" si es bisiesto. Recordar
que "un año es bisiesto si es divisible por 4, pero no por 100. Pero si es múltiplo de 400 vuelve a
ser bisiesto" 
"""

#Declaracion de variables
Año=int()
import os

#Entrada de datos
print("Bienvenido al programa, conoce si un año es o no bisiesto. . .")
Año=int(input("Cual es el año que deseas comprobar:"))

#Proceso
if Año % 4 == 0:
    print("El año ingresado es bisiesto!")

    if Año %100 != 0 and Año % 400 ==0:
        print("El año ingresado es bisiesto!")
else:
    print("El año no es bisiesto!")    

os.system('pause')
    
 