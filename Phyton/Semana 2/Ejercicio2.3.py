"""
Fundamentos de programacion D05
Ejercicio 2.3
Se desea conocer el área de un rectángulo, realizar un algoritmo que pida 
los datos correspondientes para la fórmula del área del rectángulo y dar
 como resultado dicha respuesta.  

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial


"""
#Declaración de variables
Base=Altura=Area=float()

#Entrada de datos
Base=float(input("Escribe la base del rectangulo: "))
Altura=float(input("Escribe la altura del rectangulo: "))

#Proceso
Area=Base*Altura

#Datos de salida
print("El area del rectangulo es de: " ,Area, "\n")

print("Presione cualquier tecla para finalizar")