maior = None
print(type(maior))
for i in range(5):
    numero = int(input('Informe um núemro:\n'))
    if maior is None or numero > maior:
        maior = numero

print(f'O maior valor é {maior}')
