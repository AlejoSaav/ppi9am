"""
Fundamentos de programacion D05

Ejercicio 2.10
Una modista encarga las telas al extranjero. Al pedirlo tiene que proporcionar 
las medidas de la tela en pulgadas, pero ella las tiene en metros. 
Realice un algoritmo para ayudar a resolver el problema. (1 pulgada = 0.0254 m). 


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
#Declaración de variables
CantidadMetros=PulgadasPedir=float()

#Entrada de datos

CantidadMetros=float(input("Cuantos metros requiere pedir?: "))

#Proceso
PulgadasPedir=CantidadMetros/2.54

#Datos de salida

print("La cantidad de pulgadas a pedir es de: " ,PulgadasPedir, "\n")
print("Pulse cualquier tecla para finalizar. . .")