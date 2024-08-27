# Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos.
numeros = []
soma = 0
media = 0
for i in range(10):
    numero = int(input(f'Informe o {i+1}º número:\n'))
    numeros.append(numero)
    soma += numero
media = soma / len(numeros)
print(f'O valor da média dos números digitados é {media}')
