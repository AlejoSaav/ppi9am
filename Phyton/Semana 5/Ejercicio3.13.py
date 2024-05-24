"""
Fundamentos de programacion D05
Ejercicio 3.13
Fábricas “El cometa” produce artículos con claves (1, 2, 3, 4, 5 y 6).
Costo de producción = materia prima + mano de obra + gastos de fabricación.
Precio de venta = costo de producción + 45 % de costo de producción.
La mano de obra se obtiene de la siguiente forma: para
los productos con clave 3 o 4 se carga 75 % del costo de la materia prima;
para los que tienen clave 1 y 5 se carga 80 %, y para los que tienen clave
2 o 6, 85 %.
El gasto de fabricación se considera que si el artículo
que se va a producir tiene claves 2 o 5, este gasto representa 30 % sobre
el costo de la materia prima; si las claves son 3 o 6, representa 35 %; si las
claves son 1 o 4, representa 28 %. La materia prima tiene el mismo costo
para cualquier clave.

Alumno: Samuel Alejandro Elisea Saavedra
Maestro: Conrado Cruz Gomez

Tema: Estructura de control selectiva

"""
#Declaracion de variables
MatPrima=ManObra=GastoFab=CostoProduc=Venta=float()
Clave=int()

#Entrada de datos
print("Bienvenido a fabricas El cometa")
print("Claves de articulos: 1, 2, 3, 4, 5, 6")
Clave=int(input("Cual es la clave de articulo: "))

if Clave>=1 and Clave<=6:
    MatPrima=int(input("Cual es el costo de la materia prima: "))
    if Clave==3 or Clave==4:
        ManObra=MatPrima*0.75
else:
    if Clave==1 or Clave==5:
        ManObra=MatPrima*0.80
if Clave==2 or Clave==6:
    ManObra=MatPrima*0.85

if Clave==2 or Clave==5:
    GastoFab=MatPrima*0.30
else:
    if Clave==3 or Clave==6:
        GastoFab=MatPrima*0.35
if Clave==1 or Clave==4:
    GastoFab=MatPrima*0.28

CostoProduc=MatPrima+ManObra+GastoFab
Venta=CostoProduc+(CostoProduc*0.45)

#Salida de datos
print("El gasto de la mano de obra por el articulo:",Clave, "es de $",ManObra,)
print("El gasto de fabricacion es de $",GastoFab,)
print("El costo de produccion es de $",CostoProduc,)
print("El precio de venta es de $",Venta,)