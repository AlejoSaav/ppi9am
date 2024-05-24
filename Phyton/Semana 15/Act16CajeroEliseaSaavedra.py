import os, time 
import numpy as np
from datetime import datetime
global date
monto=[]
date=datetime.now()
def Bienvenida():
    print("\n - - - - - - - - - - - - - - - - - - - - - - -")
    print("\n\tC A J E R O   B A N E X P R I M")
    print("\n - - - - - - - - - - - - - - - - - - - - - - -")
    print()
    os.system('pause')
    os.system('cls')
    print("Bienvenido al cajero de BanExprim.")
    print("\n\tEspere un momento. . .")
    time.sleep(3)
    os.system("cls")
    MenuPrincipal()
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
    CrearContraseña()
def CrearContraseña():
        os.system("cls")
        global ContraseñaNueva
        ContraseñaNueva = 0
        while True:
            try:
                print("\n Creacion de nip nuevo")
                print("Recuerde que solo deben usarse numeros")
                ContraseñaNueva = int(input("\t\n Ingresa el nip nuevo: "))
            except ValueError:
                os.system("cls")
                print("El numero es invalido...")
                time.sleep(2)
            else:
                break
        os.system("cls")
        def main():
            inicio()
        main()
def inicio():
    global Monto
    Monto=int(input("Ingresa tu monto inicial: $"))
    monto.append(Monto)

    MenuPrincipal()
def MenuPrincipal():
    os.system('cls')
    print("Bienvenido al programa, a continuacion podras seleccion entre una variedad de programas a trabajar. . .")
    Tittle=["\n\t- - - - - - - - - - Menu - - - - - - - - - -"]
    Menu=["1. Insertar Tarjeta","2. Mostrar estado","3. Depositar ","4. Retirar ","5. Recarga de saldo","6. Pago de servicios","7. Salir"]
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
           usuario()
        main()   
     if op==2:
          MostrarEstado()
     if op==3:
        def main():
           depositar()
        main()   
     if op==4:
        def main():
            retirar()
        main()
     if op==5:
        def main():
            RecargaSaldo()
        main()
     if op==6:
        def main():
            Servicios()
        main()
     if op==7:
        print("Hasta luego. . .")
        os.system('pause')
        exit() 
def MostrarEstado():
        os.system('cls')
        print("Nombre: ",Usuario,)
        print("No.Tarjeta: " ,Tarjeta)
        print("No. Detras: ",TarDetras)
        print(f"Su saldo es de: $" ,Monto, " pesos")
        print()
        print(f"Fecha de la operacion: ",date)
        os.system('pause')   
        MenuPrincipal()
def depositar():
    global Monto
    Deposito=float(input("Cantidad de dinero a depositar: $"))
    print(f"\n Se depositaron $: ",Deposito, "pesos")
    os.system('pause')
    print(f"\n Su saldo es de " ,Monto + Deposito, "pesos")
    print()
    print(f"Fecha de la operacion: ",date)
    Monto+=Deposito
    os.system('pause')
    MenuPrincipal()
def retirar():
    global Monto
    Retiro = float(input("Cantidad de dinero a retirar: $"))
    os.system('pause')
    if Monto>=Retiro:
        print(f"Se retiraron: $",Retiro, "pesos")
        print()
        print(f"El saldo es de : $",Monto-Retiro, "pesos")
        print()
        print(f"Fecha de la operacion: " ,date)
        Monto-=Retiro
        os.system('pause')
    else:
        os.system('cls')
        print("Imposible hacer ese retiro...")
        time.sleep(3)
        return Retiro
    MenuPrincipal()
def RecargaSaldo():
        os.system('cls')
        print("Bienvenido, a continuacion se te pediran datos para completar la recarga. . .")
        while True:
            try:
                Numero = int(input("Numero de celular: "))
            except ValueError:
                if Numero > 10 or Numero < 10:
                    os.system("cls")
                    print("El numero es invalido...")
                    time.sleep(2)
            else:
                break
        MenuSaldo()    
def MenuSaldo():
        os.system('cls')
        Tittle=["\n\t- - - - - - - - - - Menu - - - - - - - - - -"]
        Menu=["1. Recarga Saldo","2. Paquetes","3. Volver "]
        End=["\n\t- - - - - - - - - - - - - - - - - - - - - - -"]
        Titulo=np.array(Tittle)
        vector=np.array(Menu)
        Final=np.array(End)
  
        print(Titulo[0])
        print(vector[0])
        print(vector[1])
        print(vector[2])
        print(Final[0])
        op=int(input("Que programa desea iniciar? "))
        os.system('cls')
        while op>=1 and op<=5:
         os.system('cls')
         if op==1:
            def main():
             saldo()
            main()   
         if op==2:
          paquetes()
         if op==3:
            def main():
                MenuPrincipal()
            main()   
def paquetes():
    global Monto
    print("- - - - -  - - P a q u e t e s - - - - - - -")
    Menu=["1. Sencillo | 400 MB por $50 pesos", "2. Mediano | 1GB por $100 pesos","3. Grande | 2GB por $190 pesos","4. Estudiante | 1.3GB por $140 pesos","5. Volver"]
    vector=np.array(Menu)
    print(vector[0])
    print(vector[1])
    print(vector[2])
    print(vector[3])
    print(vector[4]) 
    op=int(input("\nQue paquete deseas comprar: "))
    os.system('cls')
    while op>=1 and op<=5:
     os.system('cls')
     if op==1:
        if Monto>50:
            print(f"Se pagaron $50 pesos.")
            print("Disfrute el paquete por un tiempo de 7 dias")
            print()
            print(f"Fecha de la operacion: " ,date,)
            Monto-=50
            os.system('pause')
            break 
        else:
         print("Saldo insuficiente...")
         time.sleep(2)
         os.system('cls')
     if op==2:
        if Monto > 100:
                print(f"\n Se pagaron $100 pesos.")
                print("Disfrute del paquete por un tiempo de 15 dias")
                print()
                print(f"Fecha de la operacion: " ,date,)
                Monto-=100
                os.system('pause')
                break
        else:
             print("Saldo insuficiente...")
             time.sleep(3)
             os.system('cls')
     if op==3:
        if Monto > 190:
                print(f"\n Se pagaron $190 pesos")
                print("Disfrute su paquete por un tiempo de 25 dias")
                print()
                print(f"Fecha de la operacion: ",date)
                Monto-=150
                os.system('pause')
                break
                
        else:
                print("Saldo insuficiente...")
                time.sleep(2)
                os.system('cls')   
     if op==4:
        if Monto > 140:
                print(f"\n Se pagaron $140 pesos")
                print("Disfrute su paquete por un tiempo de 20 dias")
                print()
                print(f"Fecha de la operacion: ",date)
                Monto-=140
                os.system('pause')
                break
                
        else:
                print("Saldo insuficiente...")
                time.sleep(2)
                os.system('cls')  
     if op==5: 
        MenuSaldo()
    MenuSaldo()
def saldo():
    global Monto
    print("Bienvenido, a continuacion se te pediran los datos necesarios. . .")
    rec=int(input("Cuanto dinero quieres recargar: "))
    if rec<=Monto:
        print("La recarga se realizo con exito. . .")
        Monto-=rec
    if rec>=Monto:
        print("Saldo insuficiente...")
        time.sleep(2)
        os.system('cls')
    MenuSaldo()
def Servicios():
        os.system("cls")
        global Monto
        print("- - - - -  - - S e r v i c i o s - - - - - - -")
        Menu=["1. Agua", "2. Luz","3. Telefono","4. Gas","5. Volver"]
        vector=np.array(Menu)
        print(vector[0])
        print(vector[1])
        print(vector[2])
        print(vector[3])
        print(vector[4]) 
        op=int(input("\nQue deseas realizar: "))
        os.system('cls')
        while op>=1 and op<=5:
         os.system('cls')
         if op==1 or op==2 or op==3 or op==4:
            os.system("cls")
            pago=float(input("Ingresa el monto a pagar: $"))
            os.system("cls")
            if Monto>pago:
                    print("Se realizo el pago del servicio...")
                    time.sleep(2)
                    print(f"\n se realizo un pago de: $" ,pago, "pesos en servicios")
                    print()
                    print(f"Fecha de la operacion: ",date)
                    Monto-=pago
                    os.system('pause')
                    break
                    
            else:
                    print("Saldo insuficiente...")
                    time.sleep(2)
                    os.system('cls') 
         if op==5:
                MenuPrincipal()
        Servicios()
def main():
    Bienvenida()
main()