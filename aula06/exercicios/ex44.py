# Crie um programa que peça ao usuário 10 números e exiba apenas os números pares.
par = []
for i in range(10):
    numero = int(input(f'Informe o {i+1}º número:\n'))
    if numero % 2 == 0:
        par.append(numero)
print(*par,sep='... ')
