# Crie um algoritmo que solicite ao usuário uma idade e verifique se ela é maior ou igual a 18.
print('-='*60)
print(f'{"MAIOR DE IDADE":^120}')
print('-='*60)

idade = int(input('Informe a idade do usuário:\n'))
if idade <= 17:
    print(f'O usuário tem {idade} anos e é MENOR DE 18')
elif idade == 18:
    print(f'O usuário tem idade igual a {idade} anos')
else:
    print(f'O usuário tem {idade} anos e é MAIOR DE 18')
