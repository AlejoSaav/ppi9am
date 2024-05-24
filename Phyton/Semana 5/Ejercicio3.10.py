"""
Fundamentos de programacion D05
Ejercicio 3.10
Una compañía de viajes cuenta con tres tipos de autobuses (A, B y C),
cada uno tiene un precio por kilómetro recorrido por persona, los costos
respectivos son $2.0, $2.5 y $3.0. Se requiere determinar el costo total y
por persona del viaje considerando que cuando éste se presupuesta debe
haber un mínimo de 20 personas, de lo contrario el cobro se realiza con
base en este número límite.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
Bus=str()
Kilometros=Personas=int()
Pago=PagoTotal=float()

#Entrada de datos
print("Bienvenido a la compañia de viajes. . .")
Kilometros=int(input("Cuantos kilometros va recorrer: "))
Bus=str(input("En que autobus viaja, |A, B, C|: "))
Personas=int(input("Cuantas personas viajan: "))

if Bus=='A' or Bus=='B' or Bus=='C':
    if Bus=='A':
        Pago=Kilometros*2
    if Bus=='B':
        Pago=Kilometros*2.5
    if Bus=='C':
        Pago=Kilometros*3

if Personas<=20:
    PagoTotal=Pago*20
else:
    PagoTotal=Pago*Personas


#Salida de datos
print("El total a pagar por el autobus es de :$",PagoTotal,)
print("El pago por persona es de:$",PagoTotal/Personas,)


