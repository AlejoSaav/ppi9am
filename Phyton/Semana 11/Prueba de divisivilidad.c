#include <studio.h>
int main()
{
    int n1,n2;
    printf("Esceiba el primer numero deseado: ");
    scanf("%i" ,&n1);
    printf("Escribe el segundo numero deseado: ");
    scanf("%i",&n2)
    if (n1 % n2 == 0)

    {
        printf("El numero %i es divisible entre %i",n1,n2);
    }
    return 0;
}