# Escreva um programa que solicite ao usuário uma lista de 5 números e exiba o maior e o menor número dessa lista.

numeros = []

for numero in range(5):
    numero = int(input(f'Informe o {numero+1}º número:\n'))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')