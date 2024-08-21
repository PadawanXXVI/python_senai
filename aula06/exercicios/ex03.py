# Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) e exiba o nome do dia correspondente.

dia = input('Informe o dia da semana [1 a 7]: ')
match dia:
    case '1':
        print(f'{dia} - domingo')
    case '2':
        print(f'{dia} - segunda')
    case '3':
        print(f'{dia} - terça')
    case '4':
        print(f'{dia} - quarta')
    case '5':
        print(f'{dia} - quinta')
    case '6':
        print(f'{dia} - sexta')
    case '7':
        print(f'{dia} - sábado')
    case _:
        print('Valor inválido')

