"""
Fundamentos de programación 
Sección D05
Ejercicio
Validar un correo

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez
Tema: Estructuras de control 
"""
import os 

signos = ['.','_','-']
numeros = ['0','1','2','3','4','5','6','7','8','9']
dominios = ['gmail', 'hotmail', 'live', 'outlook']
minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
mayusculas = []
extenciones = ['mx','ac','ad', 'ae','af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd',
    'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bl', 'bm', 'bn', 'bo', 'br', 'bq', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn',
    'es','com','org','net', 'edu']

for x in minusculas:
    mayusculas.append(x.upper())

print("\nBienvenido al programa, a continuacion se te pediran los datos. . .\n")
email = input("Escribe un correo para validar: ")
correo = ""

if email.find('@') != -1:
    nuevo_email = email.split('@')
    usuario = nuevo_email[0]
    resto = nuevo_email[1]
    continuacion = resto.split('.')
    dominio = continuacion[0]
    terminacion = continuacion[1]

    for x in usuario:
        if x in signos or x in numeros or x in minusculas or x in mayusculas:
            if dominio in dominios:
                if terminacion in extenciones:
                    correo = "El correo es correcto "
                else:
                    correo += "Puede ser valido"
            else:
                correo += "El dominio no es reconocido pero puede ser privado"
        else:
            correo += "El valor" , x , "no es valido para un correo"
        
        
else:
     correo += "Le falta un arroba al correo"

print(correo)

os.system('pause')