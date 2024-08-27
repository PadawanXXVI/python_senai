# Escreva um programa que pergunte ao usuário uma idade e verifique se a pessoa é adolescente (entre 13 e 17 anos).

print('-='*60)
print(f'{"ADOLESCENTE":^120}')
print('-='*60)

idade = int(input('Informe a idade do usuário:\n'))

if 12 < idade < 18:
    print(f'O usuário tem {idade} anos e é "ADOLESCENTE"')
else:
    print(f'O usuário tem {idade} anos e "NÃO É ADOLESCENTE')

print('-='*60)
print(f'{"FIM DO PROGRAMA":^120}')
print('-='*60)
