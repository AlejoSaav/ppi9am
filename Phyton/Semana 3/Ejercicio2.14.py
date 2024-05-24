"""
Fundamentos de programacion D05
Ejercicio 2.14
Una empresa desea determinar el monto de un cheque que debe
proporcionar a uno de sus empleados que tendrá que ir por equis
número de días a la ciudad de Monterrey; los gastos que cubre la
empresa son: hotel, comida y 100.00 pesos diarios para otros gastos.




Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
#Declaración de variables
Dias=Hotel=Comida=GastoDiario=Total=float()

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

Dias=int(input("Cuantos dias va permanecer en Monterrey: "))
Hotel=float(input("Cual es el precio del hotel por dia: "))
Comida=float(input("Cual es el gasto por comida diario: "))

#Proceso
GastoDiario=Hotel+Comida+100
Total=GastoDiario*Dias

#Salida de datos
print("El empleado gasta diariamente: ",GastoDiario, "pesos")
print("El empleado gasto en total: ",Total, "pesos\n")
print("Presione cualquier tecla para finalizar. . .")
