#include <iostream>
#include <locale.h>

using namespace std;

class Escuela{
    protected:
        char NombreMaestro[30];
        int CodigoMaestro;
        int SueldoMaestro;
        int TiempoMaestro;
        int GruposMaestro;
        int CodigoAlumno;
        char NombreAlumno[30];
        int Semestre;
        int CalificacionesAlumno;
        float promedioAlumno;
    public:
        void CapturarDatosMaestro();
        void CapturarDatosAlumno();
        void ImprimirMaestro();
        void ImprimirAlumno();
        Escuela();
        ~Escuela();


};

class Maestro: public Escuela{
    public:
        void CalcularSueldo();
        Maestro();
        ~Maestro();

};

class Alumno:public Escuela{
    public:
        void CalcularPromedio();
        Alumno();
        ~Alumno();

};

void Escuela::CapturarDatosMaestro(){
    setlocale(LC_ALL, "Spanish");
    cout<< "Ingrese su nombre: ";
    cin>> NombreMaestro;

    cout<< "Ingrese su código: " ;
    cin>> CodigoMaestro;

    cout<< "Ingrese los años que lleva impartiendo clases: ";
    cin>> TiempoMaestro;

    cout<< "Ingrese la cantidad de grupos que tiene al día: ";
    cin>> GruposMaestro;

}
void Maestro::CalcularSueldo(){
    int Dia;
    if (TiempoMaestro>10){
            Dia = 120 * GruposMaestro;
            SueldoMaestro = Dia * 15;
    }
     else
        if (TiempoMaestro>20){
            Dia = 210 * GruposMaestro;
            SueldoMaestro = Dia * 15;
        }
        else
            if (TiempoMaestro<10){
                Dia = 95 * GruposMaestro;
                SueldoMaestro = Dia * 15;
            }
}

void Escuela::ImprimirMaestro(){
    setlocale(LC_ALL, "Spanish");
    cout<< "Nombre: " <<NombreMaestro<<endl;
    cout<< "Código: " <<CodigoMaestro<<endl;
    cout<< "Años impartiendo clases: "<<TiempoMaestro<<endl;
    cout<< "Grupos a los que imparte clase diario: "<<GruposMaestro<<endl;
    cout<< "Sueldo quincenal: "<<SueldoMaestro<<endl;
}

Maestro::Maestro(){}
Maestro::~Maestro(){}

void Escuela::CapturarDatosAlumno(){
    setlocale(LC_ALL, "Spanish");
    cout<< "Ingresa tu nombre: ";
    cin>> NombreAlumno;

    cout<< "Ingresa tu código: ";
    cin>> CodigoAlumno;

    cout<< "Ingresa el semestre que cursas: ";
    cin>> Semestre;

    cout<< "Ingresa el número de calificaciones: ";
    cin>> CalificacionesAlumno;
}

void Alumno::CalcularPromedio(){
    setlocale(LC_ALL,"Spanish");
    float Cal, Cont = 0;
    system("cls");
    for(int i=0;i<CalificacionesAlumno;i++){
    cout<<"Ingrese la calificación "<<i+1<<": ";
    cin>>Cal;
    Cont = Cont + Cal;
    }
    promedioAlumno = Cont/CalificacionesAlumno;
}

void Escuela::ImprimirAlumno(){
    setlocale(LC_ALL, "Spanish");
    cout<< "Nombre: " <<NombreAlumno<<endl;
    cout<< "Código: " <<CodigoAlumno<<endl;
    cout<< "Número de calificaciones: "<<CalificacionesAlumno<<endl;
    cout<< "Promedio: "<<promedioAlumno<<endl;

}

Alumno::Alumno(){}
Alumno::~Alumno(){}

Escuela::Escuela(){}
Escuela::~Escuela(){}

int main()
{
    setlocale(LC_ALL, "Spanish");
     Maestro opmaestro;
     Alumno opalumno;
     int OpMenu, OpBucle;

    do{
            system("cls");
   cout<< "Bienvenido al sistema, selecciona una de las opciones a la que deseas entrar. . ."<<endl;
   cout << "1.- Maestro."<<endl;
   cout<< "2.- Alumno."<<endl;
   cout<< "3.- Salir."<<endl;
   cout<< "Seleccione el número: ";
   cin>> OpMenu;

   if (OpMenu==1){
        system("cls");
    cout<< "- - - - - L L E N A D O  D E  D A T O S - - - - - \n";
    opmaestro.CapturarDatosMaestro();
    system("pause");
    opmaestro.CalcularSueldo();
    system("cls");
    cout<< "- - - - - D A T O S - - - - - \n";
    opmaestro.ImprimirMaestro();
    system("pause");
   }
   if (OpMenu==2){
     system("cls");
    cout<< "- - - - - L L E N A D O  D E  D A T O S - - - - - \n";
    opalumno.CapturarDatosAlumno();
    system("pause");
    opalumno.CalcularPromedio();
    system("cls");
    cout<< "- - - - - D A T O S - - - - - \n";
    opalumno.ImprimirAlumno();
    system("pause");
   }
   if (OpMenu==3){
        system("cls");
    cout<< "Gracias por usar el sistema. . ."<<endl;
    cout<< "Saliendo del programa. . ."<<endl;
    system("pause");
    system("exit");
   }
   system("cls");
    cout<< "¿Deseas salir al menú?"<<endl;
    cout<< "1.- Sí."<<endl;
    cout<< "2.- No."<<endl;
    cin>> OpBucle;
    }while(OpBucle!=2);
        system("cls");
        cout<< "Gracias por usar el sistema. . ."<<endl;
        cout<< "Saliendo del programa. . ."<<endl;
        system("pause");
        system("exit");


    return 0;
}
