#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <locale.h>

void Agenda();


class Agenda{
     private:
            int Codigo;
            int Nacimiento;
            int Edad;

      public:
             void Datos ();
             void Imprimir ();
             Agenda ();


};


void Agenda::Datos(){

    std::cout << "Ingresa tu código de estudiante: ";
    std::cin>> Codigo;
    std::cout<< "Ingresa el año de nacimiento: ";
    std::cin>> Nacimiento;
    std::cout<< "Ingresa tu edad: ";
    std::cin>> Edad;


}
void Agenda::Imprimir() {

    cout<< "Codigo de estudiante: " <<Datos();

}




int main () {

       Agenda.op;

       op.Datos();

       op.Imprimir ();

       return 0;

}
