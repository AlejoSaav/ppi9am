a=b=c=int
suma1=suma2=suma3=c1=c2=c3=float
grupos=int(input("Ingresa el total de grupos: "))
suma3 = 0
for a in range (1, grupos + 1):
	alumnos=int(input("Ingresa el total de alumnos: "))
	suma2 = 0
	for b in range(alumnos +1):
		materias=int(input("Ingresa el total de materias: "))
		suma1 = 0
		for c in range (materias +1):
		 c1,=int(input("Ingresa las calificaciones: "))
                   c2=int(input("Ingresa las calificaciones: "))
          c3=int(input("Ingresa las calificaciones: "))
suma1 = suma1 + (c1+c2+c3)/3
			
print("El promedio del alumno ",b," es: ",suma1/materias)
suma2 = suma2 + (suma1/materias)
		
print("El promedio del grupo ",a," es: ",suma2/alumnos)
suma3 = suma3 + (suma2/alumnos)
	
print("El promedio de los ",grupos," grupos es: ",suma3/grupos)
