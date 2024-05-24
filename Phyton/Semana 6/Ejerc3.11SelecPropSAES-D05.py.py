"""
Fundamentos de programacion D05
Ejercicio 3.11
Se les dará un bono por antigüedad a los empleados de una tienda. 
Si tienen un año, se les dará $100; si tienen 2 años, $200, y así
sucesivamente hasta los 5 años. Para los que tengan más de 5, el
bono será de $1000.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaración de variables
Bono=Antiguedad=int()
import os
#Entrada de datos
Antiguedad=int(input("Cuantos años llevas trabajando: "))

if Antiguedad==1:
    Bono=100
if Antiguedad==2:
    Bono=200
if Antiguedad==3:
    Bono=300
if Antiguedad==4:
    Bono=400
if Antiguedad==5:
    Bono=500
if Antiguedad>5:
    Bono=1000
    


#Salida de datos
print("El bono por" ,Antiguedad, "año(s) es de $",Bono,)
os.system('pause')
