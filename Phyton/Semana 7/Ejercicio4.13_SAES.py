"""
Fundamentos de programación 
Sección D05

Ejercicio 4.13
Una persona adquirió un producto para pagar en 20 meses. El primer mes
pagó $10, el segundo $20, el tercero $40 y así sucesivamente. Realice un
algoritmo para determinar cuánto debe pagar mensualmente y el total de
lo que pagó después de los 20 meses

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
#Declaracion de variables
Total=Pago=int()

import os

Total = 0
for i in range (1, 21):
    print("Dia", i)
    if i==1:
        Pago=10
    else:
        Pago=Pago*2
    Total=Total+Pago
    print ("El pago es de $" ,Pago,)
    os.system('pause')
    os.system('cls')
print ("El pago total por" ,i, "meses fue de $" ,Total,)
os.system ('pause')