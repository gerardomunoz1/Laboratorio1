#include <stdio.h>

int main ()
{
	//int uvaA, uvaB; // tamaño1, tamaño2;
	char otro;
	
	
	printf ("¿La uva es A o B?: ");
	scanf ("%c", &otro);
	
	switch (otro){
		case 'a':
			printf ("La uva es de tipo A.");
			
			break;
		case 'b':
			printf ("La uva es de tipo B.");
			break;
		default:
			printf ("La opción ingresada no es válida.");
			break;
		}
		
		
	return 0;
}
	
	
		
