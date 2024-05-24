"""
Fundamentos de programacion D05
Ejercicio 2.11
La compañía de luz y sombras (CLS) requiere determinar el pago
que debe realizar una persona por el consumo de energía eléctrica,
la cual se mide en kilowatts (KW).

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
#Declaración de variables
KWUsados=PrecioKW=PagoTotal=float()

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

KWUsados=float(input("Cuantos KW consumio: "))
PrecioKW=float(input("Cual es el precio por KW: "))

#Proceso
PagoTotal=KWUsados*PrecioKW

#Salida de datos
print("El paso por el uso de: " ,KWUsados, "KW es de: " ,PagoTotal, "\n")
print("Pulse cualquier tecla para salir. . .")