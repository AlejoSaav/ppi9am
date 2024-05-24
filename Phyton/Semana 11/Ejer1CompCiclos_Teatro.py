import os, msvcrt, sys
descuentosCategoria_1 = 0
descuentosCategoria_2 = 0
descuentosCategoria_3 = 0
descuentosCategoria_4 = 0
descuentosCategoria_5 = 0
    
print("Bienvenido a la taquilla, a continuacion se piden los datos. . .")
precio_unico = float (input ("\nIngrese el precio del boleto: "))
tecla_repetir = b's'
while tecla_repetir==b's' or tecla_repetir==b'S':
 os.system ('cls')
edad = float (input ("Ingresa la edad: "))
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
os.system ('pause')