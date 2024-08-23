# Escreva um programa que peça ao usuário um número e verifique se ele é positivo, negativo ou zero.
numero = int(input('Informe um número:\n'))

if numero > 0:
    print(f'{numero} é POSITIVO')
elif numero == 0:
    print('O número digitado é "zero"')
else:
    print(f'{numero} é negativo')

