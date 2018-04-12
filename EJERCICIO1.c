/*Algoritmo narrado:
 * 1.- Ingresar el dato del candidato que desea elegir.
 * 2.- Cada voto se suma y se guarda en dicha variable.
 * 3.- Al presionar la tecla "F", se para el proceso de votación.
 * 4.- Imprimir el ganador de la votación.
 * 5.- Retornar a 0.
 *  */


#include <stdio.h>
#include <stdlib.h>

int main ()
{
	int voto, nulo=0;
	int candidato1=0, candidato2=0, candidato3=0;
	char fin='a';
	
	
	printf ("==Bienvenido al Sistema Electrónico de Votos===\n");
	printf ("==Vote por el candidato que más le represente==\n");
	printf ("Los candidatos para las elecciones 2018 son: \n");
	printf ("1.- Julio Triviño\n");
	printf ("2.- Policarpo Avendano\n");
	printf ("3.- Juan Carlos Bodoque\n");
	
	while (fin!='f'){
		printf ("Ingrese su voto: ");
		scanf ("%d", &voto);
		system ("/usr/bin/clear");
		switch (voto){
			case 1:
				printf ("Su voto fue registrado exitosamente.\n");
				candidato1 ++;
				break;
			case 2:
				printf ("Su voto fue registrado exitosamente.\n");
				candidato2 ++;
				break;
			case 3:
				printf ("Su voto fue registrado exitosamente.\n");
				candidato3 ++;
				break;
			default:
				printf ("La opción ingresada no es válida.\n");
				nulo ++;
		}
		while (getchar()!='\n');
		printf ("¿Desea seguir votando? (a = Sí // f = No): ");
		scanf ("%c", &fin);
			
	}
		printf ("Cantidad de votos nulos: %d \n", nulo);
		if ((candidato1 > candidato2) || (candidato2 > candidato3)){
			printf ("El candidato ganador es Julio Triviño con: %d votos.", candidato1);
			printf ("¡FELICITACIONES!");
		}
		
		else if ((candidato2 > candidato3) || (candidato3 > candidato1)){
			printf ("El candidato ganador es Policarpo Avendano con: %d votos", candidato2);
			printf ("¡FELICITACIONES!");
		}
		
		else if ((candidato3 > candidato1) || (candidato1 > candidato2)){
			printf ("El candidato ganador es el Juan Carlos Bodoque con: %d votos", candidato3);
			printf ("¡FELICITACIONES!");
		}
	return 0;
}
