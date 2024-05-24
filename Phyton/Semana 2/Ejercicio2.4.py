"""
Fundamentos de programacion D05
Ejercicio 2.4
Se desea conocer la circunferencia que tiene una figura cualquiera, realizar un algoritmo
 que pida los datos correspondientes para la fórmula y proyectar el resultado. 

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial


"""
#Declaración de variables
Radio=Area=float()
Pi=3.1416

#Entrada de datos
Radio=float(input("Escribe el radio de la circunferencia: "))

#Proceso 
Area=Pi*Radio*Radio

#Salida de datos
print("El area de la circunferencia es de: " ,Area, "\n")

print("Pulsa cualquier tecla para finalizar. . .")