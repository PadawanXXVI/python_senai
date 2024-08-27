# Escreva um programa que peça ao usuário para inserir uma palavra e verifique se ela tem mais de 5 letras.

print('-='*60)
print(f'{"TAMANHO DA PALAVRA":^120}')
print('-='*60)

palavra = str(input('Digite uma palavra:\n'))

if len(palavra) > 5:
    print(f'{palavra} tem mais de 5 letras')
elif len(palavra) == 5:
    print(f'{palavra} tem 5 letras')
else:
    print(f'{palavra} tem menos de 5 letras')

