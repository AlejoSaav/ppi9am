"""
Fundamentos de programación 
Sección D05

Ejercicio 4.1
Un profesor tiene un salario inicial de $1500, y recibe un incremento de 
10 % anual durante 6 años. ¿Cuál es su salario al cabo de 6
años? ¿Qué salario ha recibido en cada uno de los 6 años?

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
#Variables
Salario=int()
x=float()
Salario=1500

#Entrada de datos

for x in range (1 , 6 + 1):
    Salario= Salario + (Salario * .10)
    print("El salario en el año" ,x, "es de $" ,Salario,)

print("El salario en 6 años es de $" ,Salario,)