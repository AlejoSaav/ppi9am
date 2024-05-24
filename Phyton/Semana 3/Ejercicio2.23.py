"""
Fundamentos de programacion D05
Ejercicio 2.23
El hotel “Cama Arena” requiere determinar lo que le debe cobrar a
un huésped por su estancia en una de sus habitaciones.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
#Declaración de variables
Dias=PrecioDia=Pago=float()

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

Dias=int(input("Cuantos dias se quedo el husped: "))
PrecioDia=float(input("Cual es el precio por dia del hotel: "))

#Proceso
Pago=Dias*PrecioDia

#Salida de datos
print("Por hospedarse" ,Dias, "dias, el pago es de: ",Pago, "pesos\n")
print("Presione cualquier tecla para finalizar. . .")
