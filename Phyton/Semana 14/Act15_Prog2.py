from email import charset
import os, msvcrt, sys, __future__, statistics, time
import statistics
import numpy as np 
import random
from telnetlib import EL
from re import M
os.system("cls")

A = []
B = []
VC = [] * 20
VF = [] * 20
def validarMatriz():
    while True:
        global F
        global C
        try:
             print("\t\n Tabla con un maximo de 20x20.")

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
def crearMatriz(TN,TM):
    for i in range(TN):
        A.append([])
        for j in range(TM):
          A[i].append([None])
    print("Creacion exitosa...")
    time.sleep(3)
    os.system("cls")
    Menu()
def llenarDatos(TN,TM):
    global Sumas
    global Suma
    global rango1
    global rango2
    global rango3
    Elementos = 0
    Suma = 0
    Po = 0
    rango1 = 0
    rango2 = 0
    rango3 = 0
    for i in range(TN):
        for j in range(TM):
            if i == j:
                A[i][j] = random.randrange(1,100)
                Elementos += A[i][j]
                Suma += 1
            else:
                A[i][j] = random.randrange(1,100)
                Po += A[i][j]
                Suma += 1
            if A[i][j] >= 60 and A[i][j] <= 75:
             rango1 += 1
            elif A[i][j] >= 76 and A[i][j] <= 90:
              rango2 += 1
            elif A[i][j] > 90:
             rango3 += 1
    Sumas = Elementos + Po
    os.system('cls')
    print(f"La matriz fue hecha" ,TN, "x" ,TM,)
    time.sleep(4)
    Menu()
def Mostrar(TN,TM):
    for f in range(TN):
        for c in range(TM):
            print(A[f][c], end=("\t"))
        print()
    print()
    print(f"La suma por" ,Suma, "numeros es de: " ,Sumas,)
    print()
    print(f"Numeros dentro del rango 1 (60 - 75): " ,rango1,)
    print()
    print(f"Numeros dentro del rango 2 (76 - 90): " ,rango2,)
    print()
    print(f"Numeros dentro del rango 3 (mayores a 90): " ,rango3,)
    os.system("pause")
    os.system("cls")
    Menu()
def Bienvenida():
     print("Bienvenido al programa, a continuacion podras elaborar una matriz para que esta realice una accion. . .")
     time.sleep(1)
     os.system('pause')
     os.system('cls')
     def main():
      Menu()
     main()

def Despedida():
    
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
   
def Menu():
    os.system("cls")
    print("A continuacion se presenta en menu con el que podras trabajar en esta seccion. . .")
    Tittle=["\n\t- - - - - - - - - - Menu - - - - - - - - - -"]
    Menu=["a) Validar matriz","b) Llenar datos","c). Mostrar matriz","d). Salir del programa "]
    End=["\n\t- - - - - - - - - - - - - - - - - - - - - - -"]
    Titulo=np.array(Tittle)
    vector=np.array(Menu)
    Final=np.array(End)
    print(Titulo[0])
    print(vector[0])
    print(vector[1])
    print(vector[2])
    print(vector[3])
    print(Final[0])
    op=str(input("Que programa desea iniciar? "))
    os.system('cls')
    while op=='a' and op=='b' and op=='c' and op=='d' and op=='e':
     os.system('cls')
    if op=='a':
        def main():
           validarMatriz()
           crearMatriz(F,C)
        main()   
    if op=='b':
          llenarDatos(F,C)
    if op=='c':
        def main():
           Mostrar(F,C)
        main()   
    if op=='d':
        def main():
           Despedida()
        main()  

def SumaF():
    Suma = int()
    print()
    for f in range(F):
        Suma = 0
        for c in range(M):
            Suma += A[f][c]
        VF[f] = Suma
    time.sleep(5)

def SumaC():
    Suma = int()
    print()
    for c in range(C):
        Suma = 0
        for f in range(F):
            Suma += A[f][c]
        VC[c] = Suma
    print(f"EL TOTAL DE LA SUMA POR COLUMNA ES DE = [{VC}]")
def main():
    Bienvenida()
main()