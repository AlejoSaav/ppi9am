"""
Fundamentos de programacion D05
Ejercicio 2.6
Se desea conocer el área de una figura, para conseguirla, dicha figura está conformada por 3 figuras:
 2 triángulos rectángulos y un semicírculo. Faltando un dato por encontrar que sería la altura del
 triángulo. Se requiere un algoritmo para resolver el problema y conocer el área de la figura. 

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
import math

#Declaración de variables
Radio=Hipo=Cateto=AT=AC=Area=float()
Pi=3.1416

#Entrada de datos
Radio=float(input("Escribe el radio del semicirculo: "))
Hipo=float(input("Escribre la medida de la hipotenusa del triangulo: "))

#Proceso
Cateto=math.sqrt(Hipo*Hipo)-(Radio*Radio)
AT=2*(Radio*Cateto)/2
AC=Pi*(Radio*Radio)/2
Area=AT+AC

#Salida de datos
print("El area de la figura es de: " ,Area, "\n")
print("Presione cualquier tecla para finalizar. . .")
