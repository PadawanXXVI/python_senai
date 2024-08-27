# Crie um programa que peça ao usuário para inserir números até que ele digite o número 0. Ao final, exiba a soma de todos os números inseridos (exceto o 0).
soma = 0
while True:
    numero = int(input("Informe um número [0 para terminar]:\n"))
    if numero == 0:
        break
    soma += numero
print(f'A soma dos números informados é {soma}')
