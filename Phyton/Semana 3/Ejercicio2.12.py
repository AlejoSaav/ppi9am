"""
Fundamentos de programacion D05
Ejercicio 2.12
determinar cuánto pagará finalmente una persona
por un artículo equis, considerando que tiene un descuento de 20%,
y debe pagar 15% de IVA (debe mostrar el precio con descuento y el
precio final).


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""

#Declaración de variables
Articulo=Descuento=PagoTotal=int()

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

Articulo=int(input("Cual es el precio del articulo que comprara:"))

#Proceso
Descuento=Articulo-(Articulo*0.20)
PagoTotal=Descuento+(Descuento*0.15)

#Salida de datos
print("\nEl pago por el articulo con descuento es de: " ,Descuento,)
print("El pago total por el articulo es de: " ,PagoTotal, "\n")
print("Presione cualquier tecla para salir. . .")