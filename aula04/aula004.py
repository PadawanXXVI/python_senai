# Criando comandos de entrada com a função input
'''
print('')
print('-='*60)
print(f'{"FORMULÁRIO DE CADASTRO":^120}')
print('-='*60)
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
sexo = input('Digite o seu sexo: ')

print(f'{nome}, do sexo {sexo}, possui {idade} anos.')

print('-='*60)
print(f'{"CÁLCULO DA ÁREA DO TRIÂNGULO":^120}')
print('-='*60)

base = int(input('Informe a base do triângulo em cm: '))
altura = int(input('Informe a altura do triângulo em cm: '))
area = base*altura/2
print(f'A área do triângulo é: {int(area)}')
'''

print('-='*60)
print(f'{"CÁLCULO DO VALOR DE DELTA":^120}')
print('-='*60)
a = int(input('Informe o valor do coeficiente "a": '))
b = int(input('Informe o valor do coeficiente "b": '))
c = int(input('Informe o valor do coeficiente "c": '))
delta = b**2 - 4*a*c
print(f'O valor de delta é {delta}')
