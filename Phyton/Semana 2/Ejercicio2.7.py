"""
Fundamentos de programacion D05
Ejercicio 2.7
Un productor de leche lleva un registro de producción en litros, pero al venderlo lo pagan en 
galones. Realizar un algoritmo que ayude al productor a saber cuánto ganaría 
en un día de ventas. (1 galón = 3.875 litros) 

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
#Declaración de variables
Litros=PrecioGa=CanGalon=Ganancia=float()



#Entrada de datos
Litros=float(input("Cuantos litros produjo: "))
PrecioGa=float(input("Cual es el precio del galon: "))

#Proceso
CanGalon=(Litros/3.875)
Ganancia=PrecioGa*CanGalon

#Salida de datos
print("Las ganancias del día son de:" ,Ganancia, "\n")
print("Pulse cualquier tecla para finalizar. . .")
