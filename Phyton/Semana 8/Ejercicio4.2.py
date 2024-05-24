"""
Fundamentos de programación 
Sección D05

Ejercicio 4.2
“El náufrago satisfecho” ofrece hamburguesas sencillas (S), dobles
(D) y triples (T), las cuales tienen un costo de $20, $25 y $28 respectivamente. 
La empresa acepta tarjetas de crédito con un cargo de 5 % sobre la compra.
Suponiendo que los clientes adquieren N
hamburguesas, las cuales pueden ser de diferente tipo, realice un
algoritmo para determinar cuánto deben pagar.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
import os
import sys
#Variables
Hamburguesas=int()
PagoTotal=x=float()
PagoTotal=0

#Entrada de datos
Hamburguesas=int(input("Cuantas hamburguesas desea comprar? "))
for x in range (1, Hamburguesas + 1):
    print("Pedido" ,x,)
    print("El menu es el siguiente: ")
    print("\t1.-Hamburguesa sencilla | $20 \n\t2.-Hamburguesa doble | $25 \n\t3.-Hamburguesa triple | $28")
    sys.stdout.write ('\t')
    Tipo = 0
    while Tipo <1 or Tipo>3:
        Tipo = int (input ("Cual sera el pedido? "))
        if Tipo <1 or Tipo>3:
            sys.stdout.write ("Valor incorrecto. Ingresalo nuevamente un numero:")
    costo=0
    if Tipo==1:
        costo=20
    if Tipo==2:
        costo=25
    if Tipo==3:
        costo=28
    print ("Metodo de pago.")
    print ("\t1.- Efectivo  |\t2.-Tarjeta")
    sys.stdout.write ('\t')
    FormaPago = 0
    while FormaPago<1 or FormaPago>2:
        FormaPago = int (input ("Cual sera el metodo de pago? "))
        if FormaPago<1 or FormaPago>2:
            sys.stdout.write ("Valor incorrecto. Ingresalo nuevamente un numero: ")
    if FormaPago==1:
        cargo=0
    else:
        cargo=costo*0.05
    PagoTotal=PagoTotal+costo+cargo
    print ("El cargo es de $",cargo,)
    
    
print ("El pago total es de $" ,PagoTotal,)
os.system ('pause')

