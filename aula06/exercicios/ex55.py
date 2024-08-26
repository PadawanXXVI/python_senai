# Desenvolva um programa que peça ao usuário para inserir um número maior que 100. Se o número for menor ou igual a 100, continue pedindo até que um número maior que 100 seja inserido.
msg = 'Informe um número maior que 100:\n'
while True:
    numero = int(input(msg))
    if numero <= 100:
        numero = int(input(msg))
    else:
        break
print('FIM DE EXECUSÂO')
