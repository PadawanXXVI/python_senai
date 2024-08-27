# Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5.
print()
numero1 = int(input('Informe o primeiro número:\n'))
numero2 = int(input('Informe o segundo número:\n'))

if numero1 % 5 ==0 and numero2 % 5 == 0:
    print(f'Os números {numero1} e {numero2} são múltiplos de 5.')
elif numero1 % 5 == 0 and numero2 % 5 != 0:
    print(f'{numero1} é múltiplo de 5 e {numero2} não é múltiplo de 5')
else:
    print(f'{numero1} não é múltiplo de 5 e {numero2} é múltiplo de 5')
    