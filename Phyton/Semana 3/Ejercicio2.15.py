"""
Fundamentos de programacion D05
Ejercicio 2.14
Se desea calcular la potencia eléctrica de circuito de la figura 2.6.
Considere que: P = V*I y V = R*I.


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
#Declaración de variables
Resistencia=Intensidad=Diferencia=Potencia=float()

#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

Resistencia=float(input("Cual es la resistencia(R): "))
Intensidad=float(input("Cual es la intensidad de la corriente(I): "))

#Procesos
Diferencia=Resistencia*Intensidad
Potencia=Diferencia*Intensidad

#Salida de datos
print("La potencia del circuito es de: ",Potencia,"Amperios\n")
print("Presione cualquier tecla para finalizar. . .")
