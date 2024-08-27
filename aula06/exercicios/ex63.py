# Desenvolva um algoritmo que peça ao usuário para inserir 5 números, adicione-os a uma lista e, depois, exiba a soma de todos os números na lista.
numeros =[]
soma = 0

for numero in range(5):
    numero = int(input(f'Informe o {numero+1}º número:\n'))
    numeros.append(numero)
    soma += numero

print(f'Os números digitados foram: {numeros} e a soma deles é: {soma}')
