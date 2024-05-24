"""
Fundamentos de programación 
Sección D05

Ejercicio 4.8
Realice el algoritmo para determinar cuánto pagará una persona que
adquiere N artículos, los cuales están de promoción. Considere que
si su precio es mayor o igual a $200 se le aplica un descuento de 15%,
y si su precio es mayor a $100 pero menor a $200, el descuento es de
12%; de lo contrario, sólo se le aplica 10%. Se debe saber cuál es el
costo y el descuento que tendrá cada uno de los artículos y finalmen-
te cuánto se pagará por todos los artículos obtenidos.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
import os

pagoTotal = 0
n = int (input ("Cuantos articulos son? "))
for i in range (1, n + 1):
    print ("Articulo" ,i,)
    precio = float (input ("Cual es el precio? $: "))
    descuento=precio*0.1
    if precio>=200:
        descuento=precio*0.15
    if precio>100 and precio<200:
        descuento=precio*0.12
    costo=precio-descuento
    pagoTotal=pagoTotal+costo
    print ("Descuento: " ,descuento,)
    print ("Pago con descuento: " ,costo,)
    
    
print ("Pago total: " ,pagoTotal,)
os.system ('pause')