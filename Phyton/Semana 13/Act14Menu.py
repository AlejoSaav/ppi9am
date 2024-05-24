import os, msvcrt, sys, __future__, statistics
import statistics
import numpy as np
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