/* Algoritmo narrado.
 * 1.- Ingresar el total de la cuenta y la cantidad de personas
 * que se presentaron a comer.
 * 2.- Calcular el IVA y propina.
 * 3.- Calcular el precio que pagará cada integrante.
 * 4.- Imprimir el valor obtenido.
 * 5.- Retornar a 0.
 * */


#include <stdio.h>

int main ()
{
	int total, grupo, preciogrupal, preciofinal, precioapagar;
	float iva = 0.19;
	float propina = 0.10;
	
	printf ("+==Calculador del total a pagar==+\n");
	printf ("¿Cuántos se presentaron a comer?: ");
	scanf ("%d", &grupo);
	
	printf ("¿Cuánto fue el total de la cuenta?: ");
	scanf ("%d", &total);
	
	preciogrupal = (total * iva) + total;
	preciofinal = (preciogrupal  * propina ) + preciogrupal;
	precioapagar = preciofinal / grupo;
	
	printf ("El total de la cuenta es: %d\n pesos.", preciofinal);
	printf ("El total a pagar por cada uno es: $%d pesos.", precioapagar);
	return 0;
}
	
