# Crie um algoritmo que solicite ao usuário um número e continue pedindo outro número até que um número negativo seja inserido.

while True:
    numero = int(input('Digite um número:\n'))
    if numero < 0:
        break
print('FIM DA EXECUÇÂO')
