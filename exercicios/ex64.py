# Crie uma lista com 10 números aleatórios e exiba apenas os números que são múltiplos de 3.

from random import randint
print()
print('-='*40)
listaNumeros = []
for numero in range(10):
    numero = randint(1,1000)
    print(numero, end='... ')
    if numero % 3 == 0:
        listaNumeros.append(numero)
print(f'\nOs números múltiplos de 3 são: {listaNumeros}')
print('-='*40)



