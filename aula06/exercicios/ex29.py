# Crie um algoritmo que pergunte ao usuário um número e verifique se ele é múltiplo de 3.

print('-='*60)
print(f'{"NÚMERO MULTIPLO DE 3":^120}')
print('-='*60)

numero = int(input('Informe um número:\n'))

if numero % 3 == 0:
    print(f'{numero} é múltiplo por 3')
else:
    print(f'{numero} não é múltiplo de 3')

print('-='*60)
print(f'{"FIM DO PROGRAMA":^120}')
