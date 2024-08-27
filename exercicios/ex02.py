# Escreva um programa que peça ao usuário para inserir um número e verifique se o número é maior que 10.

print()
print('-='*60)
print(f'{"Maior que 10":^120}')
print('-='*60)

numero = int(input('Informe um número: '))
if numero > 10:
    print(f'{numero} é maior que 10')
elif numero == 10:
    print(f'{numero} é igual a 10')
else:
    print(f'{numero} é menor que 10')

