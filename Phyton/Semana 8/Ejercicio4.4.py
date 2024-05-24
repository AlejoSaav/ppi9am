"""
Fundamentos de programación 
Sección D05

Ejercicio 4.4
Una compañía fabrica focos de colores (verdes, blancos y rojos). Se
desea contabilizar, de un lote de N focos, el número de focos de cada
color que hay en existencia.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control ciclicas 
"""
import os
import sys

focosVerdes = 0
focosBlancos = 0
focosRojos = 0
n = int (input ("Cuantos focos seran? " ))
for i in range (1, n + 1):
    print ("Foco"  ,i,)
    print ("Selecciona un color.")
    print ("\t1.- Verde \n\t2.- Blanco \n\t3.- Rojo")
    
    sys.stdout.write ('\t')
    color = 0
    while color<1 or color>3:
        color = int (input ("Que color desea? "))
        if color<1 or color>3:
            sys.stdout.write ('Valor incorrecto. Ingresalo nuevamente.')
    if color==1:
        focosVerdes=focosVerdes+1
    if color==2:
        focosBlancos=focosBlancos+1
    if color==3:
        focosRojos=focosRojos+1

os.system('cls')
print ("Focos de color verde: " ,focosVerdes,)
print ("Focos de color blancos: " ,focosBlancos,)
print ("Focos de color Rojo: " ,focosRojos,)
os.system ('pause')