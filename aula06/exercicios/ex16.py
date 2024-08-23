# Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e exiba o preço correspondente por litro.

print('-='*60)
print(f'{"PREÇO DO COMBUSTÍVEL":^120}')
print('-='*60)

combustivel = int(input('''
ESCOLHA O COMBUSTÍVEL CONFORME ABAIXO:
    1 - Gsolina
    2 - Etanol
    3 - Diesel
'''))

match combustivel:
    case 1:
        print('O preço médio do litro da GASOLINA é R$ 6,18')
    case 2:
        print('O preço médio do litro de Etanol é R$ 4,04')
    case 3:
        print('O preço médio do litro de Diesel é R$ 6,38')
    case _:
        print('Você escolheu um valor inválido.')    
    
print('-='*60)
print(f'{"FIM DO PROGRAMA":^120}')
print('-='*60)
