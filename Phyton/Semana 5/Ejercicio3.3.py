"""
Fundamentos de programacion D05
Ejercicio 3.3
determinar cuánto se debe pagar por equis cantidad de lápices 
considerando que si son 1000 o más el costo es de 85¢;
de lo contrario, el precio es de 90¢.


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaración de variables
CantidadLapices=PagoTotal=()
import os


#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

CantidadLapices=int(input("Cuantos lapices comprara: "))

#Proceso
if (CantidadLapices<1000):
    PagoTotal=CantidadLapices*0.85
    print("El coste por" ,CantidadLapices, "lapices es de: ",PagoTotal,"pesos\n")
elif(CantidadLapices>1000):
    PagoTotal=CantidadLapices*0.90
    print("El coste por" ,CantidadLapices," lapices es de: ",PagoTotal,"pesos\n")

os.system('pause')