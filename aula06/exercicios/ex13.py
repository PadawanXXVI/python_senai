# Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.

print('-='*60)
print(f'{"MÊS DO ANO":^120}')
print('-='*60)

mes = int(input('Escolha o mês correspondente de 1 a 12:\n'))

match mes:
    case 1:
        print('Você escolheu "JANEIRO"')
    case 2:
        print('Você escolheu "FEVEREIRO"')
    case 3:
        print('Você escolheu "MARÇO"')
    case 4:
        print('Você escolheu "ABRIL"')
    case 5:
        print('Você escolheu "MAIO"')
    case 6:
        print('Você escolheu "JUNHO"')
    case 7:
        print('Você escolheu "JULHO"')
    case 8:
        print('Você escolheu "AGOSTO"')
    case 9:
        print('Você escolheu "SETEMBRO"')
    case 10:
        print('Você escolheu "OUTUBRO"')
    case 11:
        print('Você escolheu "NOVEMBRO"')
    case 12:
        print('Você escolheu "DEZEMBRO"')
    case _:
        print('Você escolheu um valor inválido.')