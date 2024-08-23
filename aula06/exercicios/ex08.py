# Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.
print('-='*60)
print(f'{"ESTADO CIVIL":^120}')
print('-='*60)

estadoCivil = int(input('''
EScolha o Estado Civil da Pessoa:
    1 - Solteiro
    2 - Casado
    3 - Divorciado
    4 - Viúvo
    '''))

if estadoCivil == 1:
    print('O estado civil informado é SOLTEIRO')
elif estadoCivil == 2:
    print('O estado civil informado é CASADO')
elif estadoCivil == 3:
    print('O estdo civil informado é DIVORCIADO')
elif estadoCivil == 4:
    print('O eatado civil é VIÚVO')
else:
    print('O estado civil informado não é um valor válido')

print('-='*60)
print(f'{"FIM DO PROGRAMA":^120}')
print('-='*60)
