# Crie um programa que peça ao usuário um número inteiro positivo e exiba todos os números de 1 até o número informado.
print()
print('-='*60)
print(f'{"LISTA DE NÚMEROS":^120}')
print('-='*60)

numero = int(input('Informe um número:\n'))
i = 1

while i <= numero:
    print(i, end='...')
    i += 1
print('FIM DO PROGRAMA')

