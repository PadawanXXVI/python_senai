# Escreva um programa que peça ao usuário para inserir três números e verifique se todos são iguais
print()
print('-='*60)
print(f'{"VERIFICA SE OS NÚMEROS SÃO IGUAIS":^120}')
print('-='*60)

numeros = []

for i in range(3):
    numero = int(input(f'Informe o {i+1}º número:\n'))
    numeros.append(numero)

if numeros[0] == numeros[1] == numeros [2]:
    print(f'Os números {numeros[0]}, {numeros[1]} e {numeros[2]} são iguais')
elif numeros[0] == numeros[1]:
    print(f'Os números {numeros[0]} e {numeros[1]} são iguais e diferentes de {numeros[2]}')
elif numeros[1] == numeros[2]:
    print(f'Os números {numeros[1]} e {numeros[2]} são iguais e diferentes de {numeros[0]}')
else:
    print(f'Os números {numeros[0]}, {numeros[1]} e {numeros[2]} são diferentes')

print('-='*60)
print(f'{"FIM DO PROGRAMA":^120}')
print('-='*60)


