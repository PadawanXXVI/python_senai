'''
Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.
'''
print('-='*60)
print(f'{"MEIO DE TRANSPORTE X VELOCIDADE MÉDIA":^120}')
print('-='*60)

transporte = int(input('''
INFORME O MEIO DE TRASPORTE ABAIXO:
    1 - Carro
    2 - Bicicleta
    3 - A pé
    '''))

if transporte == 1:
    print('Você escolheu CARRO e a velocidade média é de 60Km/h.')
elif transporte == 2:
    print('Você escolheu Bicicleta e a velocidade média é de 25Km/h.')
elif transporte == 3:
    print('Você escolheu À Pé e a velocidade média é de 5Km/h.')
else:
    print('Você escolheu um valor inválido')

print('-='*60)
print(f'{"FIM DO PROGRAMA":^120}')
print('-='*60)
