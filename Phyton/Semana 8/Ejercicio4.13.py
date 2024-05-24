"""
Fundamentos de programación 
Sección D05

Ejercicio 4.13
Un vendedor ha realizado N ventas y desea saber cuántas fueron
por 10,000 o menos, cuántas fueron por más de 10,000 pero por
menos de 20,000, y cuánto fue el monto de las ventas de cada una y
el monto global.


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
import os

ventas0_10000 = 0
ventas10000_20000 = 0
montoVentas0_10000 = 0
montoVentas10000_20000 = 0
montoGlobal = 0
n = int (input ("Numero de ventas: "))
for i in range (1, n + 1):
    print ("Venta " ,i,)
    venta = float (input ('Ingresa el valor la de venta: '))
    if venta<=10000:
        ventas0_10000=ventas0_10000+1
        montoVentas0_10000=montoVentas0_10000+venta
    if venta>10000 and venta<=20000:
        ventas10000_20000=ventas10000_20000+1
        montoVentas10000_20000=montoVentas10000_20000+venta
    montoGlobal=montoGlobal+venta
    print ()
print ("Ventas de 0 a 10000: " ,ventas0_10000,)
print ("Ventas de 10000 a 20000: " ,ventas10000_20000,)
print ("Monto de ventas de 0 a 10000: " ,montoVentas0_10000,)
print ("Monto de ventas de 10000 a 20000: " ,montoVentas10000_20000,)
print ("Monto global: " ,montoGlobal,)
os.system ('pause')