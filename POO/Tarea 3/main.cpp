#include <iostream>
#include <locale.h>

using namespace std;


class Empleados{
    private:
        int Id_Empleados;

    public:
        void CapturarId();
        void Imprimir();
        Empleados();
        ~Empleados();

};

class Obreros:public Empleados{
    private:
        char NombreObreros[30];
        int HrsDia;
        int Sueldo=27;
        int SueldoSemanal;
        int SueldoQuincenal;

    public:
        void CapturarObreros();
        void CalcularSueldo();
        void ImprimirObreros();
        Obreros();
        ~Obreros();

};


class Directivos:public Empleados{
private:
        char NombreDirectivos[30];


    public:
        int PuestoTrabajo;
        void CapturarDirectivos();
        void ImprimirDirectivos();
        Directivos();
        ~Directivos();

};


void Empleados::CapturarId(){
    setlocale(LC_ALL, "Spanish");
    cout<<"Escribe tu ID de empleado: "<<endl;
    cin>> Id_Empleados;

}
void Empleados::Imprimir(){
    cout<<"El ID de empleado es: " <<Id_Empleados<<endl;

}

void Obreros::CapturarObreros(){
    setlocale(LC_ALL, "Spanish");
    system("cls");
    cout<< "- - - - - O B R E R O - - - - -"<<endl;
    cout<< "Cual es tu nombre: ";
    cin>> NombreObreros;

    cout<< "Cuantas horas trabajas al día: ";
    cin>> HrsDia;

}
void Obreros::CalcularSueldo(){
    int SueldoDiario;

    SueldoDiario = Sueldo * HrsDia;
    SueldoSemanal= SueldoDiario * 5;
    SueldoQuincenal = SueldoSemanal * 3;

}

void Obreros::ImprimirObreros(){
    setlocale(LC_ALL, "Spanish");
    system("cls");
    cout<< "- - - - - O B R E R O - - - - -"<<endl;
    cout<< "Nombre del obrero: "<<NombreObreros<<endl;
    cout<< "El sueldo base por hora es de: "<<Sueldo<<endl;
    cout<< "Tu sueldo semanal fue de: "<<SueldoSemanal<<endl;
    cout<< "Tu sueldo quincenal fue de: "<<SueldoQuincenal<<endl;

}


void Directivos::CapturarDirectivos(){
    setlocale(LC_ALL, "Spanish");
    system("cls");
    cout<< "- - - - - D I R E C T I V O - - - - -"<<endl;
    cout<< "Cual es tu nombre: ";
    cin>> NombreDirectivos;

    cout<< "Seleccione el número que corresponda a su puesto de trabajo. . ."<<endl;
    cout<< "1.- Gerente de sucursal  \n2.- Jefe de unidad  \n3.- Coordinador de área \n4.- Administrativo"<<endl;
    cout<< "Número de puesto: ";
    cin>> PuestoTrabajo;

}
void Directivos::ImprimirDirectivos(){
    setlocale(LC_ALL, "Spanish");
    system("cls");
    cout<< "Nombre del obrero: "<<NombreDirectivos<<endl;
     if (PuestoTrabajo==1 or PuestoTrabajo==2){
        cout<< "Tu área de trabajo es una oficina privada"<<endl;
    }
    else
        if (PuestoTrabajo==3){
        cout<< "Tu área de trabajo son cubículos compartidos"<<endl;
    }
    else
        if (PuestoTrabajo==4){
        cout<< "Tu área de trabajo es en un escritorio"<<endl;
    }
}

Empleados::Empleados(){}
Empleados::~Empleados(){}

Obreros::Obreros(){}
Obreros::~Obreros(){}

Directivos::Directivos(){}
Directivos::~Directivos(){}



int main()
{
    int OpMenu;
    Empleados opEmpleados;
    Obreros opObreros;
    Directivos opDirectivos;


    setlocale(LC_ALL, "Spanish");
    cout << "- - - - - Bienvenido al sistema - - - - -" << endl;
    system("pause");
    system("cls");
    opEmpleados.CapturarId();
    system("pause");
    system("cls");
    cout<< "Seleccione su puesto de trabajo. . ."<<endl;
    cout<< "1.- Obrero  \n2.- Directivo"<<endl;
    cout<< "Número de puesto: ";
    cin>> OpMenu;
    system("pause");
    system("cls");
    if (OpMenu==1){
        opObreros.CapturarObreros();
        opObreros.CalcularSueldo();
        opEmpleados.Imprimir();
        opObreros.ImprimirObreros();
    }
    else
    if (OpMenu==2){
        opDirectivos.CapturarDirectivos();
        opEmpleados.Imprimir();
        opDirectivos.ImprimirDirectivos();


    }
    return 0;
}
