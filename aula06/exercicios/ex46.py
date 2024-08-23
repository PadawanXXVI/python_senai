
numero = int(input('Informe um número\n'))
print()
print('-='*15)
print(f'{"TABUADA DO NÚMERO "} {numero}')
print('-='*15)

for i in range(10):
    print(f'{numero} x {i+1} = ', numero * (i+1))
