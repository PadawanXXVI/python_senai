# Escreva um algoritmo que peça ao usuário para digitar um número e verifique se ele é maior, menor ou igual a 10.

print()
numero = int(input('Digite um número:\n'))

if numero == 10:
    print(f'{numero} é igual a 10')
elif numero < 10:
    print(f'{numero} é menor que 10')
else:
    print(f'{numero} é maior que 10')
    