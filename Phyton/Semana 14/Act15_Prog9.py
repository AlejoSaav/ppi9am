"""
Fundamentos de programacion D05
Ejercicio 9
Hacer un algoritmo que llene una matriz de 5 * 6 y que imprima cuantos de los números almacenados son ceros, cuantos
son positivos y cuantos son y cuantos son negativos.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Matrices
"""

from email import charset
import os, msvcrt, sys, __future__, statistics, time
import statistics
import numpy as np 


import os,random,time

matriz = []
VF = [0] * 6
os.system('cls')
def bienvenida():
    print("Bienvenido al programa, a continuacion podras elaborar una matriz para que esta realice una accion. . .")
    time.sleep(1)
    os.system('pause')
    os.system('cls')
    def main():
     validarMatriz()
    main()
def despedida():
    os.system("cls")

    while True:
         os.system('cls')
         print("Con esto finaliza el funcionamiento. . .")
         print("Gracias por usar este programa. . .")
         time.sleep(2)
         
         print("\na)Crear otra matriz    b)Salir del programa")
         op=str(input("Que desea hacer? "))
         os.system('cls')
         while op=='a' and op=='b':
            os.system('cls')
         if op=='a':
            def main():
             validarMatriz()
            main()   
         if op=='b':
            print("Hasta luego. . .")
            os.system('pause')
            exit()

def Error():
    print("Datos invalidos:...")

def validarMatriz():
    while True:
        global F
        global C
        try:
             print("\t\n Tabla con un maximo de 5 x 6.")

             F = int(input("Dame el numero de filas que desea agregar: "))

             C = int(input("Dame el numero de columnas que desea agregar: "))
        except ValueError:
            Error()
        else:
             if not ( F >= 2 and C <= 6) or not (F >= 2 and C <= 6):
                 Error()
             else:
                 print("Los datos son validos...")
                 print(f"La matriz de" ,F, "x" ,C, "fue creada.")
                 time.sleep(2)
                 os.system('cls')
        break
    crearMatriz(F,C)
def crearMatriz(TF,TC):
    for i in range(TF):
        matriz.append([])
        for j in range(TC):
            matriz[i].append([None])
    print("Se creo la matriz...")
    os.system("cls")
    time.sleep(3)
    llenarAutomatico(F,C)
def llenarAutomatico(TF,TC):
    global elementoNegativo
    global elementoPositivo
    global cero
    elementoPositivo = 0
    elementoNegativo = 0
    cero = 0
    for i in range(TF):
        for j in range(TC):
            if i == j:
                matriz[i][j] = random.randrange(-100,100)
                if matriz[i][j] < 0:
                     elementoNegativo += 1
                else:
                    elementoPositivo += 1
            else:
                 matriz[i][j] = random.randrange(0,100)
                 if matriz[i][j] == 0:
                      cero += 1
                 else:
                     elementoPositivo += 1
    print("Matriz con los datos...")
    time.sleep(3)
    mostrar(F,C)
def  mostrar(TF,TC):
    for f in range(TF):
        for c in range(TC):
            print(matriz[f][c], end=("\t"))
        print(VF[f])
    print()
    print(f"El total de numeros positivos son: " ,elementoPositivo,)
    print()
    print(f"El total de numeros negativos son: " ,elementoNegativo,)
    print()
    print(f"El total de numeros 0 son: " ,cero,)
    print()            
    print("\n Matriz con los datos llenados....")
    print()
    os.system("pause")
    despedida()


def main():
    bienvenida()
main()