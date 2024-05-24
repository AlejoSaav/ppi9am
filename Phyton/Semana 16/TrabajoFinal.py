"""
Carrera: Ing. En computación
Materia: Fundamentos de programación D05
Alumno: Samuel Alejandro Elisea Saavedra
Profesor: Conrado Cruz Gomez

Tema: Trabajo final | Simular una tienda de videojuegos
"""

import time, os, numpy as np
from datetime import datetime
date=datetime.now()
metodo=[]
comprador=[]
Monto=15000
empresa=[]
eleccion=[]
def bienvenida():
    print("\n - - - - - - - - - - - - - - - - - - - - - - -")
    print("\n\tTienda de Videojuego Saturn")
    print("\n - - - - - - - - - - - - - - - - - - - - - - -")
    print()
    os.system('pause')
    os.system('cls')
    print("Bienvenido a la tienda Saturn.")
    print("\n    Espere un momento. . .")
    time.sleep(4)
    menuPrincipal()
def menuPrincipal():
     os.system('cls')
     print("Bienvenido a Saturn, a continuacion podras seleccion entre una variedad de opciones. . .")
     Tittle=["\n\t- - - - - - - - - - Menu - - - - - - - - - -"]
     Menu=["1. Catalogo de juegos","2. Catalogo de consolas","3. Ofertas","4. Compra ","5. Carrito","6. Ticket de compra","7. Salir"]
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
     print(Final[0])
     op=int(input("Que requiere hacer: "))
     os.system('cls')
     while op>=1 and op<=7:
      os.system('cls')
      if op==1:
        def main():
           catalogoJuegos()
        main()   
      if op==2:
          catalogoConsolas()
      if op==3:
        def main():
           ofertas()
        main()   
      if op==4:
        def main():
            compra()
        main()
      if op==5:
        def main():
            carrito()
        main()
      if op==6:
        def main():
            ticket()
        main()
      if op==7:
        print("Hasta luego. . .")
        os.system('pause')
        exit() 
def catalogoJuegos():
    Tittle=np.array(['- - - - - - - - - - C a t a l o g o - - - - - - - - - -'])
    Barra=np.array(["            Titulo        ","          Precio           "])
    Juego1=np.array(['         Elden Ring       ','          $1,800           '])
    Juego2=np.array(['         Dark Souls       ','            $500           '])
    Juego3=np.array(['         Destiny 1       ','            $1,000          '])


    print(Tittle[0])
    print(Barra)
    print(Juego1)
    print(Juego2)
    print(Juego3)
    os.system('pause')
    menuPrincipal()
def catalogoConsolas():
    Tittle=np.array(['- - - - - - - - - - C a t a l o g o - - - - - - - - - -'])
    Barra=np.array(["            Consola        ","          Precio           "])
    Consola1=np.array(['         Xbox One S       ','          $10,000           '])
    Consola2=np.array(['         PlayStation 5       ','       $15,,000           '])
    Consola3=np.array(['         Nintendo Switch      ','      $15,500           '])


    print(Tittle[0])
    print(Barra)
    print(Consola1)
    print(Consola2)
    print(Consola3)
    os.system('pause')
    menuPrincipal()
def ofertas():
    print("Bienvenido a las ofertas especiales de Saturn")
    print("Podras encontrar una variedad de ofertas que quiza sean de tu agrado. . .")
    os.system('pause')
    os.system('cls')
    print("Lo sentimos, en este momento no hay ofertas disponibles :(")
    os.system('pause')
    menuPrincipal()
def bienvenidaCompra():
    os.system('cls')
    print("Redirigiendo a la aplicacion de transaccion. . .")
    print("\n\tEspero un momento por favor.")
    time.sleep(3)
    usuario()
def compra():
    global Nombre
    global Pago
    global pagoEfec
    print("A continuacion se te pedira llenar una serie de datos para completar tu compra")
    Nombre=str(input("Nombre: "))
    comprador.append(Nombre)
    os.system('cls')
    print("A continuacion por favor escribe el nombre del juego/consola que deseas. . .")
    Eleccion=str(input("Cual es la compra: "))
    eleccion.append(Eleccion)
    os.system('cls')
    print("A continuacion se te pedira el metodo de pago que haras")
    print("En esta tienda se acepta dos metodos: Efectivo o por transaccion desde una aplicacion")
    os.system('pause')
    os.system('cls')
    Pago=str(input("Forma de pago: "))
    metodo.append(Pago)
    if Pago=='Efectivo' or 'efectivo':
        pagoEfec=float(input("Precio de la compra hecha: "))
        os.system('cls')
        print("Se hizo un pago en efecto de $",pagoEfec)
    if Pago=='Transaccion' or 'transaccion':
        def main():
            bienvenidaCompra()
        main()
    else: 
        print("Metodo de pago incorrecto, por favor escribe uno correcto. . .")
    menuPrincipal()
def transaccion():
    os.system('cls')
    print("- - - - - - - - - - B a n c o - - - - - - - - - -")
    print("Bienvenido a la aplicacion de transacciones, a continuacion podras seleccion entre una variedad de opciones. . .")
    Tittle=["\n\t- - - - - - - - - - Menu - - - - - - - - - -"]
    Menu=["1. Estado de cuenta","2. Transaccion","3. Salir"]
    End=["\n\t- - - - - - - - - - - - - - - - - - - - - - -"]
    Titulo=np.array(Tittle)
    vector=np.array(Menu)
    Final=np.array(End)
  
    print(Titulo[0])
    print(vector[0])
    print(vector[1])
    print(vector[2])
    print(Final[0])
    op=int(input("Que requiere hacer: "))
    os.system('cls')
    while op>=1 and op<=7:
      os.system('cls')
      if op==1:
        def main():
           estadoCuenta()
        main()   
      if op==2:
          deposito()
      if op==3:
        def main():
           menuPrincipal()
        main()   
def usuario():
    global Usuario
    global Tarjeta
    global TarDetras
    os.system("cls")
    while True:
        try:
            Usuario=str(input("Ingresa tu nombre: "))
        except ValueError:
            os.system("cls")
            print("No puede tener numeros o simbolos...")
            print("\t\nEspere un momento. . .")
            time.sleep(2)
            
        else:
            break
    while True:
        try:
            Tarjeta=int(input("Ingresa los digitos de su tarjeta de credito: "))
            TarDetras=int(input("Ingresa los 3 digitos de la parte de atras: "))
            
        except ValueError:
            if Tarjeta<1000000000000000:
                print("Los digitos de la tarjeta son invalidos...")
                time.sleep(3)
            elif TarDetras<99:
                print("Digitos invalidos...")
                time.sleep(2)
        else:
            break
    transaccion()
def estadoCuenta():
        global Monto
        os.system('cls')
        print("Nombre: ",Usuario,)
        print("No.Tarjeta: " ,Tarjeta)
        print("No. Detras: ",TarDetras)
        print(f"Su saldo es de: $" ,Monto, " pesos")
        print()
        print(f"Fecha de la operacion: ",date)
        os.system('pause')   
        transaccion()
def deposito():
    global Monto
    global Residuo
    global Retiro
    os.system('cls')
    Empresa=str(input("A quien se dirige la transaccion: "))
    empresa.append(Empresa)
    Retiro = float(input("Cantidad de dinero a transferir: $"))
    os.system('pause')
    if Monto>=Retiro:
        print(f"Se retiraron: $",Retiro, "pesos")
        print()
        Residuo= Monto-Retiro
        print(f"El saldo es de : $",Residuo, "pesos")
        print()
        print(f"Fecha de la operacion: " ,date)
        Monto-=Retiro
        os.system('pause')
    else:
        os.system('cls')
        print("Imposible hacer ese retiro...")
        time.sleep(3)
        return Retiro
    transaccion()
def carrito():
    global Nombre
    os.system('cls')
    print("- - - - - Carrito de compras - - - - -")
    print("Bienvenido ",Nombre, "aqui se mostraran las compras que haz realizado. . .")
    print("Se agrego: ",eleccion)
    os.system('pause')
    menuPrincipal()
def ticket():
    global Nombre
    global pagoEfec
    os.system('cls')
    print("- - - - - - - - - - T i c k e t - - - - - - - - - -")

    print("Nombre: " ,Nombre)
    print("Forma de pago: ",metodo)
    print("Compra: ",eleccion)
    if metodo =='Transaccion' or 'transaccion':
         print("Se Transfirio a ",empresa)
         print(f"Se pagaron: $",Retiro, "pesos por el juego/consola")
         print()
    else: 
        print("Se realizo un pago en efectivo de $" ,pagoEfec)
    os.system('pause')
    
    menuPrincipal()



def main():
    bienvenida()
main()