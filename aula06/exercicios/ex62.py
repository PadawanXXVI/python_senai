# Escreva um programa que solicite ao usuário para inserir 3 nomes e armazene-os em uma lista. Em seguida, imprima a lista completa.

nomes = []

for nome in range(3):
    nome = str(input(f'Informe o {nome+1}º nome:\n')).upper()
    nomes.append(nome)
print(f'A lsita dos nomes é: {nomes}')