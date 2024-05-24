"""
Fundamentos de programacion D05
Ejercicio 3.12
El consultorio del Dr. Lorenzo T. Mata Lozano tiene como política cobrar
la consulta con base en el número de cita, de la siguiente forma:
• Las tres primeras citas a $200.00 c/u.
• Las siguientes dos citas a $150.00 c/u.
• Las tres siguientes citas a $100.00 c/u.
• Las restantes a $50.00 c/u, mientras dure el tratamiento.
Se requiere un algoritmo para determinar:
a) Cuánto pagará el paciente por la cita.
b) El monto de lo que ha pagado el paciente por el tratamiento.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaración de variables
NumConsulta=PrecioTotal=int()
import os 

#Entrada de datos
print("Bienvenido al consultorio del Dr. Lorenzo T. Mata Lozano. . .")
NumConsulta=int(input("Que numero de consulta tiene: "))

#Proceso
if NumConsulta<=3:
    CostoConsulta=200
    PrecioTotal=CostoConsulta*NumConsulta
    print("El precio de la consulta es de:" ,CostoConsulta, "pesos")
    print("El costo total del tratamiento es de: ",PrecioTotal, "pesos")

elif NumConsulta<=5:
    CostoConsulta=150
    PrecioTotal=(NumConsulta - 3) * 150 + 600
    print("El costo de la consulta es de:" ,CostoConsulta, "pesos")
    print("El costo total del tratamiento es de: ",PrecioTotal, "pesos")

elif NumConsulta<=8:
    CostoConsulta=100
    PrecioTotal=(NumConsulta - 5) * 100 + 900
    print("El costo de la consulta es de:" ,CostoConsulta, "pesos")
    print("El costo total del tratamiento es de: ",PrecioTotal, "pesos")

else:
    CostoConsulta=50
    PrecioTotal=(NumConsulta - 8) * 50 + 1200
    print("El costo de la consulta es de:" ,CostoConsulta, "pesos")
    print("El costo total del tratamiento es de: ",PrecioTotal, "pesos")

#Salida de datos
os.system('pause')


    


