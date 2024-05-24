n = suma = calBaja = float()
x = int()
suma = 0
calBaja = 0
for x in range (1, 40 + 1):
    n = float(input("Cual es la calificacion: "))
    if x == 1:
        calBaja = n
    else:
        if n < calBaja:
            calBaja = n

    suma = suma + n

print("La calificacion media del grupo es de: ",suma/40,)
print("La calificacion mas baja del grupo es: ",calBaja,) 