#  Escreva um algoritmo que peça ao usuário um número de 1 a 5 e verifique se ele é igual a 3.

numero = int(input('Informe um núemro entre 1 e 5:\n'))

if numero not in range(1,6):
    print('Número inválido')
if numero in range(1,6):
    if numero == 3:
        print(f'{numero} é igual a 3')
    else:
        print(f'{numero} é diferente de 3')
