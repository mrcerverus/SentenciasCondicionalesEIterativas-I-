""" importacion libreria random """
import random

""" listado de variables """
myList = ["Piedra" , "Papel" , "Tijera"]
resultado = ""
jugador = ""

""" Argumento Inválido """
while True:
    jugador = input('''Elije entre ["Piedra" , "Papel" , "Tijera"]: \n''').title()
    if jugador not in myList:
        print('''Argumento inválido: Debe ser ["Piedra" , "Papel" , "Tijera"].''')
        continue
    else:
        break

""" Elección del Pc """
computador = random.choice(myList)

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