# Crie um algoritmo que verifique se um número inserido pelo usuário é par ou ímpar.
print('-='*60)
print(f'{"PAR OU ÍMPAR":^120}')
print('-='*60)

numero = int(input('Escolha um número:\n'))

if numero % 2 == 0:
    print(f'{numero} é um numero PAR')
else:
    print(f'{numero} é um número ÍMPAR')    
