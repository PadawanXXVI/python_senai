# Crie um algoritmo que solicite ao usuário uma idade e verifique se ela é maior ou igual a 18.
print('-='*60)
print(f'{"MAIOR DE IDADE":^120}')
print('-='*60)

idade = int(input('Informe a idade do usuário:\n'))
if idade < 17:
    print(f'O usuário tem {idade} e é MENOR DE 18')
else:
    print(f'O usuário tem {idade} e é MAIOR DE 18')
