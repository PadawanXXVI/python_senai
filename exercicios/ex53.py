# Escreva um programa que peça ao usuário um número e exiba a contagem regressiva desse número até 1.

numero = int(input('Informe um número\n'))

while numero >= 1:
    print(numero, end='... ')
    numero -= 1
    