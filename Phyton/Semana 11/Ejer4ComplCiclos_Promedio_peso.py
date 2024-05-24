import os

promedioAdultos = 0
promedioJovenes = 0
promedioNinos = 0
promedioViejos = 0
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
os.system ('pause')