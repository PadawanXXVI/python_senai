# Crie um programa que pergunte ao usuário um número de 1 a 3 e exiba o nome correspondente ao número (1: "um", 2: "dois", 3: "três").

print('-=*60')
print(f'{"Número por extenso":^120}')
print('-='*60)

numero = int(input('Digite um número de 1 a 3: '))
if numero == 1:
    print('1: um')
elif numero == 2:
    print('2 = dois')
elif numero == 3:
    print('3: três')
else:
    print('Número inválido')
    

