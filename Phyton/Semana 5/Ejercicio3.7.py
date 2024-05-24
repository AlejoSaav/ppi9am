"""
Fundamentos de programacion D05
Ejercicio 3.7
La asociación de vinicultores tiene como política fijar un precio inicial al
kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2.
Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño,
se requiere determinar cuánto recibirá un productor por la uva que entrega 
en un embarque, considerando lo siguiente: si es de tipo A, se le cargan
20¢ al precio inicial cuando es de tamaño 1; y 30¢ si es de tamaño 2. Si
es de tipo B, se rebajan 30¢ cuando es de tamaño 1, y 50¢ cuando es de
tamaño 2.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaración de variables
A=B=()

TipoUva=TamañoUva=Precio=Kilo=Pago=()

#Entrada de datos
print("Bienvenido al programa, a continuacion se te pediran los datos fijos: ")
print("Tipos de uva: A y B  |  Tamaño de uva: 1 y 2\n")

TipoUva=(input("Que tipo de uva es:"))
TamañoUva=int(input("Que tamaño tiene la uva: "))
Precio=float(input("Cual es el precio del kilo de uva: "))
Kilo=float(input("Cuantos kilos fueron: "))

#Proceso
if TipoUva==A:
    if TamañoUva==1:
        Precio=Precio+0.20
else:
    Precio=Precio+0.30

if TipoUva==B:
    if TamañoUva==2:
        Precio=Precio+0.30
else:
    Precio=Precio+0.50

Pago=Kilo*Precio

#Salida de datos
print("El pago es de: ",Pago,)
    
