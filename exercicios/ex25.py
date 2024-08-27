# Escreva um programa que peça ao usuário um número de 0 a 20 e verifique se ele está entre 10 e 15.

numero = int(input('Escolha um número entre 0 e 20:\n'))

if numero not in range(0,21):
    print('<<< Valor inválido >>>')
if numero in range(0, 21):
    if 10 <= numero <= 15:
        print(f'Você digitou o número {numero} e ele está entre 10 e 15.')
    else:
        print(f'Você digitou o número {numero} e ele não está entre 10 e 15.')
    