#include <iostream>
#include <locale.h>
#include<stdio.h>
#include<conio.h>
#include<time.h>

using namespace std;


class Edad{
    private:
        int DD;
        int MM;
        int AA;
    public:
        void CapturarDatos();
        void Imprimir();
        Edad();
        ~Edad();

};

void Edad::CapturarDatos(){
    setlocale(LC_ALL, "Spanish");
    system("cls");
    cout<< "Ingresa el día de nacimiento: ";
    cin>> DD;
    cout<< "Ingresa el mes de nacimiento: ";
    cin>> MM;
    cout<< "Ingresa el año de nacimiento: ";
    cin>>AA;

}

void Edad::Imprimir(){
    int Resultado;
   setlocale(LC_ALL, "Spanish");
   system("cls");
   cout<< "Día de nacimiento: " <<DD ;
   cout<< "\n Mes de nacimiento: " <<MM ;
   cout<< "\n Año de nacimiento: " <<AA ;
   cout<< "\n Edad actual: ";


}

Edad::Edad(){}
Edad::~Edad(){}

int main()
{
    int elec;

    do{
    Edad op;

    op.CapturarDatos();
    op.Imprimir();

    system("pause");
    system("cls");
    cout<< "Deseas salir del programa?"<<endl;
    cout<< "1.- Si"<<endl;
    cout<< "2.- No"<<endl;
    cout<< ":";
    cin>> elec;

    }while(elec!=1);

    cout<< "Saliendo del programa";

    return 0;
}
