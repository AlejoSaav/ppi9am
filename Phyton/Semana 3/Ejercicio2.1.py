"""
Fundamentos de programacion D05
Ejercicio 2.1
Realice un algoritmo para obtener el área de un triángulo.


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
#Declaración de variables
Altura=Base=Area=int()

#Entrada de datos

print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

Altura=int(input("Escribe la altura del triangulo: "))
Base=int(input("Escribe la base del triangulo: "))

#Proceso
Area=Base*Altura/2

#Salida de datos
print("El area del triangulo es de: " ,Area, "\n")

print("Pulsa cualquier tecla para finalizar. . .")
