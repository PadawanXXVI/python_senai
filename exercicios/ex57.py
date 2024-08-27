# Crie um programa que peça ao usuário para adivinhar um número secreto entre 1 e 10. Continue pedindo até que ele adivinhe o número corretamente.

from random import randint
computador = randint(1,10)


while True:
    jogador = int(input('Informe um número de 1 a 10:\n'))
    if jogador == computador:
        print('Parabéns! Você acertou!')
        break
    else:
        print("Você errou, tente novamente!")