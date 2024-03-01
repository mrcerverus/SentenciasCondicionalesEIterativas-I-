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
        break

""" Evaluación juego """
if jugador == computador:
    resultado = "Empataste"
elif (jugador == "Piedra" and computador == "Tijera") or \
    (jugador == "Tijera" and computador == "Papel") or \
    (jugador == "Papel" and computador == "Piedra"):
    resultado = "Ganaste"
else:
    resultado = "Perdiste"

""" Resultado en pantalla """
while True:
    if jugador not in myList:
        break
    else:
        print(f'''
        Tu jugaste {jugador}
        Computador jugó {computador}.
        {resultado}!!''')
        break