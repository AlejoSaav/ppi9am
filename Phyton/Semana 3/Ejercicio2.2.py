"""
Fundamentos de programacion D05
Ejercicio 2.2
Una empresa importadora desea determinar cuántos dólares puede
adquirir con equis cantidad de dinero mexicano.


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
#Declaración de variables 
DinMex=Cambio=float()
Dolares=20.68


#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

DinMex=float(input("Pesos mexicanos que quieres cambiar: "))

#Proceso 
Cambio=DinMex/Dolares

#Salida de datos
print("Tus" ,DinMex, "pesos mexicanos valen: " ,Cambio, "dolares \n")
print("Pulse cualquier tecla para finalizar. . .")
