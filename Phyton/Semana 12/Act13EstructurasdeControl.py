"""
Fundamentos de programación 
Sección D05


Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Actividad complementaria ciclos
"""
import os, msvcrt, sys, __future__, statistics
import statistics
import numpy as np 

def menu():
  Tittle=["\n\t- - - - - - - - - - Menu - - - - - - - - - -"]
  Menu=["1.Teatro","2. Media de calificacion","3. Reloj","4. Promedio de peso ","5. Cantidad de hombres/mujeres","6. Color de placas ","7. Promedio de calificacion grupal ","8.  Promedio de edades ","9. Numero mayor y menor","10. Promedio de calificaciones","11. Salir del programa"]
  End=["\n\t- - - - - - - - - - - - - - - - - - - - - - -"]
  Titulo=np.array(Tittle)
  vector=np.array(Menu)
  Final=np.array(End)
  
  print(Titulo[0])
  print(vector[0])
  print(vector[1])
  print(vector[2])
  print(vector[3])
  print(vector[4])
  print(vector[5])
  print(vector[6])
  print(vector[7])
  print(vector[8])
  print(vector[9])
  print(vector[10])
  print(Final[0])
  eleccion=int(input("\nIngrese el numero del programa: "))
  os.system('cls')
  if eleccion==1:
    def main():
        teatro()
    main()
  if eleccion==2:
    def main():
       calificacion()
    main()
  if eleccion==3:
     def main():
        reloj()
     main()
  if eleccion==4:
    def main():
       PromPeso()
    main()
  if eleccion==5:
     def main():
        PromGen()
     main()
  if eleccion==6:
    def main():
       placa()
    main()
  if eleccion==7:
     def main():
        PromCalificaciones()
     main()
  if eleccion==8:
    def main():
       PromEdad()
    main()
  if eleccion==9:
     def main():
        MayorMenor()
     main()
  if eleccion==10:
    def main():
       PromEscolar()
    main() 
  if eleccion==11:
     print("Saliendo del programa. . .")
     os.system('pause')
def teatro():
    Lista=[]
    descuentosCategoria_1 = 0
    descuentosCategoria_2 = 0
    descuentosCategoria_3 = 0
    descuentosCategoria_4 = 0
    descuentosCategoria_5 = 0
    i=0
    print("Bienvenido a la taquilla, a continuacion se piden los datos. . .")
    precio_unico = float (input ("\nIngrese el precio del boleto: "))
    tecla_repetir = b's'
    while tecla_repetir==b's' or tecla_repetir==b'S':
     os.system ('cls')
     edad = float (input ("Ingresa la edad: "))
     Lista.append(edad)
     i = i + 1
     descuento=0
     if edad<5:
        print ("No puede entrar al teatro, no cumple la edad requerida")
     if edad>=5 and edad<15:
        descuento=precio_unico*0.35
        descuentosCategoria_1=descuentosCategoria_1+descuento
     if edad>=15 and edad<20:
        descuento=precio_unico*0.25
        descuentosCategoria_2=descuentosCategoria_2+descuento
     if edad>=20 and edad<46:
        descuento=precio_unico*0.1
        descuentosCategoria_3=descuentosCategoria_3+descuento
     if edad>=46 and edad<66:
        descuento=precio_unico*0.25
        descuentosCategoria_4=descuentosCategoria_4+descuento
     if edad>=66:
        descuento=precio_unico*0.35
        descuentosCategoria_5=descuentosCategoria_5+descuento
     print ("El descuento es de: " ,descuento,)
     print('Deseas repetir el proceso? (S/N): ')
     sys.stdout.write 
     tecla_repetir = b'\0'
     while tecla_repetir!=b's' and tecla_repetir!=b'S' and tecla_repetir!=b'n' and tecla_repetir!=b'N':
      tecla_repetir = msvcrt.getch ()
    print ("Descuentos por categoria 1: " ,descuentosCategoria_1,)
    print ("Descuentos por categoria 2: " ,descuentosCategoria_2,)
    print ("Descuentos por categoria 3: " ,descuentosCategoria_3,)
    print ("Descuentos por categoria 4: " ,descuentosCategoria_4,)
    print ("Descuentos por categoria 5: " ,descuentosCategoria_5,)
    print("Las edades ingresadas fueron: ",Lista)
    print ("Desea salir al menu o seguir en el programa? \t1. Salir\t2. Seguir en el programa ")
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
           teatro()
        main()
def calificacion():
 print("Bienvenido al programa para calcular la media y la calificacion mas baja de un grupo de estudiantes")
 
 
 n = suma = calBaja = promedio = float()
 x = int()
 suma = 0
 i = 1

 calBaja = 0
 for x in range (1, 40 + 1):
    n = float(input("Cual es la calificacion: "))
    
    if x == 1:
        calBaja = n
    else:
        if n < calBaja:
            calBaja = n

    suma = suma + n

 

 print("La calificacion media del grupo es de: ",suma/40)
 print("La calificacion mas baja del grupo es: ",calBaja,)
 
 print ("Desea salir al menu o seguir en el programa? \t1. Salir\t2. Seguir en el programa ")
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
           calificacion()
        main()
def reloj():
   print("En progreso. . .")
   print ("Desea salir al menu o seguir en el programa? \t1. Salir\t2. Seguir en el programa ")
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
           reloj()
        main()
        os.system('pause')
def PromPeso():
 promedioAdultos = 0
 promedioJovenes = 0
 promedioNinos = 0
 promedioViejos = 0
 print("Bienvenido al programa, a continuacion podras conocer el promedio de peso de niños, jovenes, adultos y viejos. . .")
 for i in range (1, 51):
    print ("Persona" ,i,)
    edad = int (input ("Ingresa la edad de la persona: "))
    peso = int (input ("Ingresa el peso: "))
    if edad>=0 and edad<=12:
        promedioNinos=promedioNinos+peso
    if edad>=13 and edad<=29:
        promedioJovenes=promedioJovenes+peso
    if edad>=30 and edad<=59:
        promedioAdultos=promedioAdultos+peso
    if edad>=60:
        promedioViejos=promedioViejos+peso
    
 promedioAdultos=100.0*promedioAdultos/50
 promedioJovenes=100.0*promedioJovenes/50
 promedioNinos=100.0*promedioNinos/50
 promedioViejos=100.0*promedioViejos/50
 print ("Promedio de adultos: " ,promedioAdultos,)
 print ("Promedio de jovenes: " ,promedioJovenes,)
 print ("Promedio de niños: "  ,promedioNinos,)
 print ("Promedio de viejos: "  ,promedioViejos,)
 print ("Desea salir al menu o seguir en el programa? \t1. Salir\t2. Seguir en el programa ")
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
           PromPeso()
        main()
def PromGen():
   hombres = 0
   mujeres = 0
   print("Bienvenido al programa, a continuacion podras saber el numero de hombres y mujeres que hay en un grupo. . .")
   n = int (input ("Ingresa el numero de alumnos: "))
   for i in range (1, n + 1):

    print ("Selecciona el numero correspondiente al genero.")
    print ("\t1.- Mujer")
    print ("\t2.- Hombre")
    sys.stdout.write ('\t')
    genero = 0
    while genero<1 or genero>2:
        genero = int (input (': '))
        if genero<1 or genero>2:
            sys.stdout.write ("Numero incorrecto. Ingresalo nuevamente.")
    if genero==1:
        mujeres=mujeres+1
    else:
        hombres=hombres+1
    print ()
   print ("Numero de hombres: " ,hombres,)
   print ("Numero de mujeres: " ,mujeres,)
   print ("Desea salir al menu o seguir en el programa? \t1. Salir\t2. Seguir en el programa ")
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
           PromGen()
        main()
def placa():
   print("En progreso. . .")
   print ("Desea salir al menu o seguir en el programa? \t1. Salir\t2. Seguir en el programa ")
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
           placa()
        main()
def PromCalificaciones():
   lista=[]

   print("Bienvenido al programa, a continuacion podras promediar la calificacion que tiene un grupo de estudiantes. . .")
   cantidadCal=int(input("Cuantas calificaciones se desea promediar: "))
   i = 1

   while(cantidadCal>0):
    numero =float(input("Calificacion " + str(i) + ": "))
    lista.append(numero)
    i = i + 1
    cantidadCal = cantidadCal - 1

   promedio = sum(lista)/len(lista)

   print("El promedio es de: ",promedio,)
   print ("Desea salir al menu o seguir en el programa? \t1. Salir\t2. Seguir en el programa ")
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
           PromCalificaciones()
        main()
def PromEdad(): 
   hombres = 0
   mujeres = 0
   promedioGrupal = 0
   promedioHombres = 0
   promedioMujeres = 0
   tecla_repetir = b's'
   while tecla_repetir==b's' or tecla_repetir==b'S':
    os.system ('cls')
    edad = int (input ("Cual es la edad de la persona: "))
    print ("Selecciona el genero.")
    print ('\t1.- Hombre')
    print ('\t2.- Mujer')
    sys.stdout.write ('\t')
    genero = 0
    while genero<1 or genero>2:
        genero = int (input (': '))
        if genero<1 or genero>2:
            sys.stdout.write ("Opcion incorrecta. Ingresa nuevamente la opcion.")
    promedioGrupal=promedioGrupal+edad
    if genero==1:
        promedioHombres=promedioHombres+edad
        hombres=hombres+1
    else:
        promedioMujeres=promedioMujeres+edad
        mujeres=mujeres+1
    print (("\nDeseas repetir el proceso? (S/N): "))
    sys.stdout.write 
    tecla_repetir = b'\0'
    while tecla_repetir!=b's' and tecla_repetir!=b'S' and tecla_repetir!=b'n' and tecla_repetir!=b'N':
        tecla_repetir = msvcrt.getch ()
    promedioGrupal=promedioGrupal/(hombres+mujeres)
   if hombres == 0:
     promedio_hombres = 0
   else:
    promedioHombres=promedioHombres/hombres
   if mujeres == 0:
    promedioMujeres = 0
   else:
    promedioMujeres=promedioMujeres/mujeres
   print ("Numero de hombres: " ,hombres,)
   print ("Numero de mujeres: " ,mujeres,)
   print ("Promedio del grupo: " ,promedioGrupal,)
   print ("Promedio de hombres: " ,promedioHombres,)
   print ("Promedio de mujeres: " ,promedioMujeres,)
   os.system ('pause')
   print ("Desea salir al menu o seguir en el programa? \t1. Salir\t2. Seguir en el programa ")
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
           PromEdad()
        main()
def MayorMenor():
   lista=[]
   print("Bienvenido al programa, a continuacion podras conocer el numero mayor y menor de una secuencia de numeros. . .")
   cantidadNum=int(input("Cuantos numeros desea ingresar: "))
   mayor= 0
   menor = 0
   i = 1

   while(cantidadNum>0):
    numero =float(input("Numero " + str(i) + ": "))
    lista.append(numero)
    i = i + 1
    cantidadNum = cantidadNum - 1
   mayor = max(lista)
   menor = min(lista)

   print("Numeros ingresados" ,lista,)
   print("El numero mayor es: " ,mayor,)
   print("El numero menor es: " ,menor,)
   print ("Desea salir al menu o seguir en el programa? \t1. Salir\t2. Seguir en el programa ")
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
           MayorMenor()
        main()
def PromEscolar():
   
   print("En progreso. . .")
   
   print ("Desea salir al menu o seguir en el programa? \t1. Salir\t2. Seguir en el programa ")
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
           PromEscolar()
        main()
        
    


Presentacion=["Bienvenido al programa, a continuacion se te mostrara el menu con los distintos programas. . ."]
Inicio=np.array(Presentacion)

print(Inicio[0])

def main():
   menu()
main()
   