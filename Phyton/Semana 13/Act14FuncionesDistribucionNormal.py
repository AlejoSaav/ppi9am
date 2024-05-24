import os, msvcrt, sys, __future__, statistics
import statistics
import numpy as np 
import math


def menu():
    print("Bienvenido al programa, a continuacion se te mostrara el menu con el que podras trabajar. . .")
    Tittle=["\n\t- - - - - - - - - - Menu - - - - - - - - - -"]
    Menu=["\n1. Calcular la desviacion estandar", "2. Calcular la media ", "3. Calcular la propabilidad", "3. Salir del programa"]
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
    eleccion=int(input("\nIngrese el numero del programa: "))
    os.system('cls')
    if eleccion==1:
     def main():
         desviacionEstandar()
     main()
    if eleccion==2:
     def main():
       media()
     main()
    if eleccion==3:
     def main():
       ProbabilidadF()
     main()
    if eleccion==4:
     print("Saliendo del programa. . .")
     os.system('pause')
def desviacionEstandar():
    lista= []
    print("Bienvenido al programa, a continuacion podras ingresar los datos a trabajar. . .")
    cantidadNum=int(input("Cuantos numeros deseas ingresar: "))
    i = 1

    while(cantidadNum>0):
     numero =float(input("Numero " + str(i) + ": "))
     lista.append(numero)
     i = i + 1
     cantidadNum = cantidadNum - 1
     

    mean = sum(lista) / len(lista)
    var = sum((l-mean)**2 for l in lista) / len(lista)
    st_dev = math.sqrt(var)
    print("La desviacion media de los datos es de: " + str(st_dev))
    
    print ("\nDesea salir al menu o seguir en el programa? \t1. Salir\t2. Seguir en el programa ")
    sys.stdout.write ('\t')
    
    op = 0
    while op<1 or op>2:
        op = int (input (': '))
        if op<1 or op>2:
            sys.stdout.write ("Numero incorrecto. Ingresalo nuevamente.")
    os.system('cls')
    if op==1:
        def main():
           menu()
        main()   
    else:
        def main():
           desviacionEstandar()
        main()  
def media():
    lista= []
    print("Bienvenido al programa, a continuacion podras ingresar los datos para sacar la media. . .")
    cantidadNum=int(input("Cuantos numeros deseas ingresar: "))
    i = 1

    while(cantidadNum>0):
     numero =float(input("Numero " + str(i) + ": "))
     lista.append(numero)
     i = i + 1
     cantidadNum = cantidadNum - 1
     
    promedio = sum(lista)/len(lista)

    print("El promedio es de: ",promedio,)
    print ("\nDesea salir al menu o seguir en el programa? \t1. Salir\t2. Seguir en el programa ")
    sys.stdout.write ('\t')
    op = 0
    while op<1 or op>2:
        op = int (input (': '))
        if op<1 or op>2:
            sys.stdout.write ("Numero incorrecto. Ingresalo nuevamente.")
    os.system('cls')
    if op==1:
        def main():
           menu()
        main()   
    else:
        def main():
           media()
        main()
def ProbabilidadF():
    
    lista=[]

    print("Bienvenido al programa, a continuacion podras calcular la probabilidad de una cantidad de numeros que selecciones. . .")
    cantidadCal=int(input("Cuantos numeros se desea calcular la probabilidad: "))
    i = 1

    while(cantidadCal>0):
     numero =float(input("Numero " + str(i) + ": "))
     lista.append(numero)
     i = i + 1
     cantidadCal = cantidadCal - 1
    
    print("Lo sentimos, en progreso de terminar. . .")
      

     
    print ("\nDesea salir al menu o seguir en el programa? \t1. Salir\t2. Seguir en el programa ")
    sys.stdout.write ('\t')
    op = 0
    while op<1 or op>2:
        op = int (input (': '))
        if op<1 or op>2:
            sys.stdout.write ("Numero incorrecto. Ingresalo nuevamente.")
    if op==1:
        def main():
           menu()
        main()   
    else:
        def main():
           ProbabilidadF()
        main()


def main():
    menu()
main()
