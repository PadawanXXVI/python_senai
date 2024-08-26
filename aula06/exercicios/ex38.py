# Escreva um programa que peça ao usuário para digitar sua altura em metros e verifique se ela é maior que 1.75.
print()
print('-='*60)
print(f'{"ALTURA DO USUÁRIO":^120}')
print('-='*60)

altura = float(input('Informe a sua altura em metros:\n'))

if altura > 1.75:
    print(f'O usuário tem {altura}m é é mais alto que 1.75m')
elif altura == 1.75:
    print(f'O usuário tem exatamente {altura}m')
else:
    print(f'O usuário tem {altura}m e é mais baixo que 1.75m')

print('-='*60)
print(f'{"FIM DO PROGRAMA":^120}')
print('-='*60)
