"""

LABEMAX
Ingeniería Civil en Bioinformática
Gerardo Muñoz & Benjamín Rojas

"""
import time
import os
import random

def mapita (map, posX, posY):

    for i in range (0,20):

        linea = ""

        for j in range (0,20):

            casilla = map [i][j]

            if (posX == j and posY == i):

                linea += "🦆"			#Ficha jugador

            else:
                if casilla == str (0):
                    linea += "⬜"		#Murallas

                elif casilla == str (1):
                    linea += "  "		#Nada

                elif casilla == str (3):
                    linea += "🏠"		#Inicio

                elif casilla == str (4):
                    linea += "🏁"		#Meta

                elif casilla == str (5):
                    linea += "⬛"		#Camino

        print (linea)

print ("   +--------------------------------+")
print ("   |======Bienvenido a LabeMax======|")
print ("   |==ING. CIVIL EN BIOINFORMÁTICA==|")
print ("   +--------------------------------+")
print (" ")

time.sleep (1)

print ("Eres un pato y tienes que salir del laberinto.")
time.sleep (1)
print ("¿Por qué eres un pato? Eso no me lo preguntes ;)")
time.sleep (1)
print ("Yo solo soy una computadora 😎")
time.sleep (1)
print ("\n")

map = ["10000000000000000000",
       "35555555555500005550",
       "10000500000500005000",
       "10055555555555555000",
       "10050050500500000000",
       "10050055500555505500",
       "10050050000500000500",
       "10550055000555555500",
       "10500005500000000500",
       "10000005005500000500",
       "10050005000500555500",
       "10050005000555500500",
       "10055555550000055500",
       "10050005000000000500",
       "10050005000055555500",
       "10050005000050000550",
       "10050005555555550000",
       "10055055000000055550",
       "10000000000000000050",
       "11111111111111111141"]

juego = 0
numerodejugadas = 0
posX = 1
posY = 1

print ("\t      ¿¿PREPARADO??")
print ("\n")
time.sleep (1)
os.system('clear')

print ("\t➡ ESTE ES EL LABERINTO ⬅")

time.sleep (1)

mapita (map, posX, posY)

while (juego == 0):

    opcion = input ("En que dirección se quiere mover: ")

    os.system('clear')
    print ("\t      ➡ TABLERO ⬅")
    print ("\n")

    numero_aleatorio=random.randint (0,3)

    if (opcion == 'w' or opcion == 'W'):

        if (map[posY-1][posX] != '0'):
            posY = posY -1

        else:
            print ("MOVIMIENTO NO VÁLIDO. INTENTE NUEVMANTE.")
            if (numero_aleatorio == 0):
                print ("VAMOS PATITO, TU PUEDES")

            elif (numero_aleatorio == 1):
                print ("ESCUCHA TU CORAZÓN, TU PUEDES")

            else:
                print ("¡NO TE RINDAS PATITO!")


    elif (opcion == 's' or opcion == 'S'):

        if (map[posY+1][posX] != '0'):

            posY = posY +1

        else:
            print ("MOVIMIENTO NO VÁLIDO. INTENTE NUEVMANTE.")
            if (numero_aleatorio == 0):
                print ("VAMOS PATITO, TU PUEDES")

            elif (numero_aleatorio == 1):
                print ("ESCUCHA TU CORAZÓN, TU PUEDES")

            else:
                print ("¡NO TE RINDAS PATITO!")

    elif (opcion == 'a' or opcion == 'A'):

        if (map[posY][posX-1] != '0' and map[posY][posX-1] != '3'):

            posX = posX -1

        else:
            print ("MOVIMIENTO NO VÁLIDO. INTENTE NUEVMANTE.")
            if (numero_aleatorio == 0):
                print ("VAMOS PATITO, TU PUEDES")

            elif (numero_aleatorio == 1):
                print ("ESCUCHA TU CORAZÓN, TU PUEDES")

            else:
                print ("¡NO TE RINDAS PATITO!")

    elif (opcion == 'd' or opcion == 'D'):

        if (map[posY][posX+1] != '0'):

            posX = posX +1

        else:
            print ("MOVIMIENTO NO VÁLIDO. INTENTE NUEVMANTE.")
            if (numero_aleatorio == 0):
                print ("VAMOS PATITO, TU PUEDES")

            elif (numero_aleatorio == 1):
                print ("ESCUCHA TU CORAZÓN, TU PUEDES")

            else:
                print ("¡NO TE RINDAS PATITO!")

    mapita (map, posX, posY)
    numerodejugadas = numerodejugadas +1

    print ("")

    if (map [posY][posX] == '4'):

        print ("\n")
        print ("     +--------------------------------------------------------------------+")
        print ("     |🔥💯🔥💯🔥💯🔥💯¡¡HAS LOGRADO ESCAPAR DEL LABERINTO!!💯🔥💯🔥💯🔥💯 |")
        print ("     |🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥¡¡FELICIADES!!🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥|")
        print ("     +--------------------------------------------------------------------+")
        print ("     |                      LOGRASTE SALIR EN", numerodejugadas, "JUGADAS                  |")
        print ("     +--------------------------------------------------------------------+")

        juego = 1

