"""
Fundamentos de programacion D05
Ejercicio 3.4
Almacenes “El harapiento distinguido” tiene una promoción: a todos los
trajes que tienen un precio superior a $2500.00 se les aplicará un descuento 
de 15 %, a todos los demás se les aplicará sólo 8 %.


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaración de variables
PrecioTraje=PagoTotal=()
import os 
#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

PrecioTraje=float(input("Cual es el precio del traje que compro: "))

#Proceso
if (PrecioTraje==2500):
    PagoTotal=PrecioTraje-(PrecioTraje*0.15)
    print("El precio del traje tiene un descuento del 15%. . .")
    print("Su pago con descuento sera de: ",PagoTotal," pesos\n")
if (PrecioTraje>2500):
    PagoTotal=PrecioTraje-(PrecioTraje*0.15)
    print("El precio del traje tiene un descuento del 15%. . .")
    print("Su pago con descuento sera de: ",PagoTotal," pesos\n")
elif (PrecioTraje<2500):
    PagoTotal=PrecioTraje-(PrecioTraje*0.08)
    print("El traje tiene un descuento del 8%. . .")
    print("Su pago con descuento sera de: ",PagoTotal," pesos\n")

#Salida de datos
os.system('pause')