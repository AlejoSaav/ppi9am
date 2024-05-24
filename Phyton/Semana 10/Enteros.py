from __future__ import print_function
import os
def enteros():
 num = input("\nIngrese un numero para validar: ")
 try:
      num_entero = float(num)
 except ValueError:
      num_entero = None
      
 if num_entero == None:
      print(num, "no es un numero")
 elif num_entero == int(num_entero):
      print(int(num_entero), "es un entero", )
 else:
      print(num_entero, "No es un numero entero",)


def reales():
    num = input("\nIngrese un numero para validar: ")
    try:
      num_real = float(num)
    except ValueError:
      num_real = None
      
    if num_real == None:
      print(num, "no es un numero")
    elif num_real == int(num_real):
      print(int(num_real), "es un numero real", )
    else:
      print(num_real, "es un numero real",) 
         
print("\nBienvenido al programa, a continuacion se mostrara el menu. . .\n")
print("1. - Validar numeros enteros | 2. - Validar numeros reales")
eleccion=int(input("\nQue opcion necesita? "))
if eleccion == 1:
    def main():
        enteros()
    main()
if eleccion == 2:
    def main():
        reales()
    main()
 
os.system('pause')




