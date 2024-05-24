import statistics
lista=[]

cantidadCal=int(input("Cuantas calificaciones se desea promediar: "))
i = 1

while(cantidadCal>0):
    numero =float(input("Calificacion " + str(i) + ": "))
    lista.append(numero)
    i = i + 1
    cantidadCal = cantidadCal - 1

promedio = sum(lista)/len(lista)

print("El promedio es de: ",promedio,)
