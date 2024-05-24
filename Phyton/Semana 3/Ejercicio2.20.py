"""
Fundamentos de programacion D05
Ejercicio 2.20
Determinar el promedio que obtendrá un alumno considerando que 
realiza tres exámenes, de los cuales el primero y el segundo 
tienen una ponderación de 25%, mientras que el tercero de 50%.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control secuencial

"""
#Declaración de variables
Examen1=Examen2=Examen3=Promedio=float()
Exam1=Exam2=Exam3=float()
#Entrada de datos
print("\n Bienvenido al programa, a continuacion se te pediran los datos. . ." "\n")

Examen1=float(input("Cual es la calificacion del primer examen: "))
Examen2=float(input("cual es la calificacion del segundo examen: "))
Examen3=float(input("Cual es la calificacion del tercer examen: "))

#Proceso
Exam1=Examen1*0.25
Exam2=Examen2*0.25
Exam3=Examen3*0.50
Promedio=Exam1+Exam2+Exam3

#Salida de datos
print("El promedio de las calificaciones es de: ",Promedio,"\n")
print("Presione cualquier tecla para finalizar. . .")
