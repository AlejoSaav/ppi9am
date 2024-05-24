import os, sys
hombres = 0
mujeres = 0
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
print ("Valor de hombres: " ,hombres,)
print ("Valor de mujeres: " ,mujeres,)
os.system ('pause')


