"""
Fundamentos de programacion D05
Ejercicio 2.21
Realice un diagrama de flujo y pseudocódigo que representen el algoritmo 
para determinar aproximadamente cuántos meses, semanas, 
días y horas ha vivido una persona.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
#Declaración de variables
import datetime
Nacimiento=hoy=dias=semanas=meses=horas=()

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

Nacimiento=(input("Fecha de nacimiento de la persona (Dia/Mes/Año): "))

#Proceso
Nacimiento = datetime.datetime.strptime(Nacimiento, '%d/%m/%Y').date()
hoy = datetime.date.today()
dias = (hoy-Nacimiento).days
horas = dias * 24
meses = ((hoy.year - Nacimiento.year) *12) + (hoy.month - Nacimiento.month)
semanas = int(round(dias/7, 0))

#Salida de datos
print("Dias:" ,dias,)
print("Meses:" ,meses,)
print("Semanas:" ,semanas,)
print("Horas:" ,horas,)