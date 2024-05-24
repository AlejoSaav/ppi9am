"""
Fundamentos de programacion D05
Ejercicio 3.6
“La langosta ahumada” es una empresa dedicada a ofrecer banquetes; sus
tarifas son las siguientes: el costo de platillo por persona es de $95.00,
pero si el número de personas es mayor a 200 pero menor o igual a 300,
el costo es de $85.00. Para más de 300 personas el costo por platillo es de
$75.00.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaración de variables
CantidadPersonas=PagoTotal=()
import os 

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

CantidadPersonas=int(input("Cuantas personas asistiran al evento: "))

#Proceso
if CantidadPersonas<200:
    PagoTotal=CantidadPersonas*95
    print("El costo por persona es de: 95 pesos")
    print("El pago total por el evento sera de: " ,PagoTotal," pesos\n")
elif CantidadPersonas>200:
    PagoTotal=CantidadPersonas*85
    print("El costo por persona es de: 85 pesos")
    print("El pago total por el evento sera de: " ,PagoTotal," pesos\n")
elif CantidadPersonas==300:
    PagoTotal=CantidadPersonas*85
    print("El costo por persona es de: 85 pesos")
    print("El pago total por el evento sera de: " ,PagoTotal," pesos\n")
elif CantidadPersonas>300:
    PagoTotal=CantidadPersonas*75
    print("El costo por persona es de: 75 pesos")
    print("El pago total por el evento sera de: ",PagoTotal," pesos\n")

os.system('pause')
