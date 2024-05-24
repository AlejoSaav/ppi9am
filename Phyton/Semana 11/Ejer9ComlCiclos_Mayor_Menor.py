lista=[]

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