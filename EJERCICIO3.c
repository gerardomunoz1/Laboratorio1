/*Algoritmo narrado.
 * 1.- Ingresar el precio del traje.
 * 2.- Calcular si el precio ingresado es menor o mayor a 2.500 pesos.
 * 3.- Aplicar el descuento correspondiente.
 * 4.- Imprimir el precio final con el descuento aplicado.
 * 5.- Retornar a 0.
 * */


#include <stdio.h>
#include <stdlib.h>

int main ()
{
	int valor;
	
	printf ("=====+El harapiento distinguido+=====\n");
	printf ("=====+ Calculador de descuento +=====\n");
	printf ("-------------------------------------\n");
	
	printf ("Ingrese el precio del traje: $");
	scanf ("%d", &valor);
	
	if (valor > 2500){
		valor = valor * 0.85;
	}
	
	else if (valor < 2500){
		valor = valor * 0.92;
	}
	
	printf ("Total a pagar: $%d pesos.", valor);
	
	return 0;
} 
	
