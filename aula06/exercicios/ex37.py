# Desenvolva um algoritmo que peça ao usuário para digitar um número e verifique se ele é múltiplo de 2 ou de 5.
print()
print('-='*60)
print(f'{"VERIFICA SE UM NÚMERO É MULTIPLO DE 2 OU DE 5":^120}')
print('-='*60)

numero = int(input('Informe um número:\n'))

if numero % 2 == 0 and numero % 5 == 0:
    print(f'O número {numero} é multiplo de 2 e de 5')
elif numero % 2 == 0 and numero % 5 != 0:
    print(f'O número {numero} é multiplo de 2 mas não é multiplo de 5')
else:
    print(f'O número {numero} não é múltiplo de2 mas é multiplo de 5')

print('-='*60)
print(f'{'FIM DO PROGRAMA':^120}')
print('-='*60)

