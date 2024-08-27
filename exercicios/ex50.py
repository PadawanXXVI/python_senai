# Crie um programa que peça ao usuário para inserir um número e, em seguida, exiba os números de 1 até esse número, mas de forma decrescente.
numero = int(input('Informe um número:\n'))

while numero >= 1:
    print(numero, end='... ')
    numero -= 1

print('\nFIM DO PROGRAMA')

