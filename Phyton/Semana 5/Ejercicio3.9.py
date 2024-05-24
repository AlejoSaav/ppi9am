"""
Fundamentos de programacion D05
Ejercicio 3.9
La política de la compañía telefónica “chimefón” es: “Chismea + x -”. Cuando 
se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal
forma que los primeros cinco minutos cuestan $ 1.00 c/u, los siguientes
tres, 80¢ c/u, los siguientes dos minutos, 70¢ c/u, y a partir del décimo
minuto, 50¢ c/u.
Además, se carga un impuesto de 3 % cuando es domingo, y si es
día hábil, en turno matutino, 15 %, y en turno vespertino, 10 %. Realice
un algoritmo para determinar cuánto debe pagar por cada concepto una
persona que realiza una llamada.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaracion de variables
import string


Duracion=Dia=Turno=PagoTiempo=Impuesto=PagoTotal=()
Matutino=Vespertino=()

#Entrada de datos
print("Bienvenido a la compañia telefonica chimefon, complete los datos requeridos. . .")
print("El día se solicita en numero. . .")

Duracion=int(input("Cuanto duro la llamada: "))
if Duracion<=5:
        PagoTiempo=Duracion*1
if Duracion<=8:
        PagoTiempo=(Duracion - 5) * 0.8 + 5.0
if Duracion<=10:
        PagoTiempo=(Duracion - 8) * 0.7 + 7.4
if Duracion>10:
        PagoTiempo=(Duracion - 10) * 0.5 + 8.8

print("1.- Lunes a Sabado | 2.- Domingo")
Dia=(input("Que dia fue la llamada: "))


if Dia==2:
    Impuesto=PagoTiempo*0.03

if Dia==1:
 print("1.- Turno Matutino   | 2.-Turno Vespertino ")
Turno=(input("Cual es el turno: "))

if Turno==1:
    Impuesto=PagoTiempo*0.15
else:
   Turno==2
   Impuesto=-PagoTiempo*0.10

PagoTotal=PagoTiempo+Impuesto

#Salida de datos
print("El pago por ",Duracion, "minutos es de: ",PagoTiempo, "pesos\n")
print("El pago del impuesto es de: ",Impuesto, "pesos\n")
print("El pago total es de: " ,PagoTotal, "pesos\n")
