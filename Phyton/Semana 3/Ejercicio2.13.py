"""
Fundamentos de programacion D05
Ejercicio 2.13
Determinar cuánto dinero ahorra una persona en un
año si considera que cada semana ahorra 15% de su sueldo (considere 
cuatro semanas por mes y que no cambia el sueldo).



Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
#Declaración de variables
Sueldo=SueldoSemanal=SueldoMensual=SueldoAnual=float()

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

Sueldo=float(input("Cual es el sueldo semanal que tiene: "))

#Proceso
SueldoSemanal=Sueldo*0.15
SueldoMensual=SueldoSemanal*4
SueldoAnual=SueldoMensual*12

#Salida de datos
print("Se ahorran semanalmente:" ,SueldoSemanal, "pesos")
print("El ahorro en un mes es de:" ,SueldoMensual, "pesos")
print("El ahorro durante el año es de:" ,SueldoAnual, "pesos\n")
print("Presione cualquier tecla para finalizar. . .")