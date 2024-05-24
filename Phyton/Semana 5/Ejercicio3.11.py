"""
Fundamentos de programacion D05
Ejercicio 3.11
“El náufrago satisfecho” ofrece hamburguesas sencillas, dobles y triples,
las cuales tienen un costo de $20.00, $25.00 y $28.00 respectivamente. La
empresa acepta tarjetas de crédito con un cargo de 5 % sobre la compra.
Suponiendo que los clientes adquieren sólo un tipo de hamburguesa, realice 
un algoritmo para determinar cuánto debe pagar una persona por N hamburguesas.
Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaracion de varibles
Hamburguesa=Cantidad=Precio=Met=int()
PagoTotal=Cargo=float()

#Entrada de datos
print("Bienvenido al naufrago satisfecho...")

Cantidad=int(input("Cuantas hamburguesas va comprar: "))
print("----------Menu----------")
print("1.-Hamburguesa sencilla | $20.00\n2.-Hambuerguesa doble | $25.00\n3.-Hambuerguesa triple | $28.00")
Hamburguesa=int(input("Que menu comprara: "))
if Hamburguesa==1:
    PagoTotal=Cantidad*20
else:
 if Hamburguesa==2:
    PagoTotal=Cantidad*25
 else:
  if Hamburguesa==3:
   PagoTotal=Cantidad*28

print("\n-----Metodo de pago-----")
print("1.- Efectivo | 2.- Tarjeta de credito")
Met=int(input("Como va pagar: "))
if Met==1:
    print("Por" ,Cantidad, "hamburguesas se debe pagar $",PagoTotal,)
else:
 if Met==2:
    Cargo=PagoTotal*0.05
    print("Por" ,Cantidad, "hamburguesas el pago es de $",PagoTotal+Cargo,)
    print("El cargo aplicado fue de $",Cargo,)

