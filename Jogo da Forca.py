import random
import TemasSorteio


TEMA = random.choice(list(TemasSorteio.temas.keys()))
palavraSorteada = random.choice(TemasSorteio.temas[TEMA])

palavra = palavraSorteada
letras_palavra = []
vidas = 4
vitoria = False
from termcolor import colored
from colorama import init

init()

def printCor(msg, cor):
    print(colored(msg, cor))


printCor(f'O TEMA É: {TEMA.upper()}', cor ='blue')

while True:
    for letra in palavra:
        if letra in letras_palavra:
            print(letra, end = '')
        else:
            print('-', end = '')
    print()
    tentativa = str(input(colored('Digite a sua letra: ', 'yellow'))).lower().strip()
    letras_palavra.append(tentativa)
    if tentativa not in palavra:
        vidas -= 1
        printCor('ERROU!', 'red')
    printCor('++' * 10, 'green')
    printCor(f'Você tem {vidas} vidas', 'yellow')

    vitoria = True
    for letra in palavra:
        if letra not in letras_palavra:
            vitoria = False

    if vidas < 1 or vitoria:
        printCor('GAME OVER!', 'cyan')
        break

if vitoria:
    print(f'parabéns você ganhou. A palavra era {palavra}')
else:
    print(f'Você perdeu. A palavra era {palavra}')