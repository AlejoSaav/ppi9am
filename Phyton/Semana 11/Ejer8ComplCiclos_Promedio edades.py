import os, msvcrt, sys

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