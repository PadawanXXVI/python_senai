# Desenvolva um programa que peça ao usuário para inserir 7 números e, ao final, exiba quantos desses números são maiores que 10
maior10 = []
for i in range (7):
    numero = int(input(f'Informe o {i+1}º número:\n'))
    if numero > 10:
        maior10.append(numero)
print(f'O total de números maiores que 10 que foram digitados é {len(maior10)}')
