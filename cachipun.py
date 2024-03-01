""" importacion libreria random """
import random
import sys

""" listado de variables """
myList = ["Piedra" , "Papel" , "Tijera"]
resultado = ""
jugador = ""

""" Elección del Pc """
computador = random.choice(myList)

""" Argumento Inválido """
while True:
    jugador = sys.argv[1].title() 
    # input('''Elije entre ["Piedra" , "Papel" , "Tijera"]: \n''').title()
    if jugador not in myList:
        print('''Argumento inválido: Debe ser ["Piedra" , "Papel" , "Tijera"].''')
        break
    else:
        """ Evaluación juego """
        if jugador == computador:
            resultado = "Empataste"
        elif jugador == "Piedra" and computador == "Tijera":
            resultado = "Ganaste"
        elif jugador == "Piedra" and computador == "Papel":
            resultado = "Perdiste"
        elif jugador == "Tijera" and computador == "Piedra":
            resultado = "Perdiste"
        elif jugador == "Tijera" and computador == "Papel":
            resultado = "Ganaste"
        elif jugador == "Papel" and computador == "Tijera":
            resultado = "Perdiste"
        elif jugador == "Papel" and computador == "Piedra":
            resultado = "Ganaste"

        """ Resultado en pantalla """
        print(f'''
        Tu jugaste {jugador}
        Computador jugó {computador}.
        {resultado}!!''')