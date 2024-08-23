# Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if.
print('-='*60)
print(f'{"SISTEMA DE CLASSIFICAÇÃO":^120}')
print('-='*60)

nota = int(input('Escolha uma nota de 0 a 10:\n'))
if nota < 5:
    print(f'A nota {nota} é uma nota BAIXA ')
elif 5 <= nota <= 7:
    print(f'A nota {nota} é uma nota MÉDIA')
else:
    print(f'A nota {nota} é uma nota ALTA')

print('-='*60)
print(f'{"FIM DO PROGRAMA":^120}')
print('-='*60)