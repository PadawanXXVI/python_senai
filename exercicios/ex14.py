# Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a soma deles é maior que 100.

print('-='*60)
print(f'{"SOMA MAIOR QUE 100"}')
print('-='*60)

numero1 = int(input('Informe o primeiro número:\n'))
numero2 = int(input('Informe o segundo número:\n'))
soma = numero1 + numero2

if soma > 100:
    print(f'A soma de {numero1} e {numero2} é {soma}. Esse valor é MAIOR QUE 100')
else:
    print(f'A soma de {numero1} e {numero2} é {soma}. Esse valor é MENOR QUE 100')

print('-='*60)
print(f'{"FIM DO PROGRAMA":^120}')
print('-='*60)
