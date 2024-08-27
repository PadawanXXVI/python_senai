# Escreva um algoritmo que peça ao usuário para inserir 5 números e, ao final, exiba o maior número inserido.

print('-='*60)
print(f'{"MAIOR VALOR":^120}')
print('-='*60)

maior = None
print(type(maior))
for i in range(5):
    numero = int(input('Informe um número:\n'))
    if maior is None or numero > maior:
        maior = numero

print(f'O maior valor é {maior}')

print('-='*60)
print(f'{"FIM DO PROGRAMA":^120}')
print('-='*60)

