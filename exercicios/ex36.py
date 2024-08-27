# Crie um programa que solicite ao usuário um número de 1 a 12 e exiba o mês correspondente.
print('-='*60)
print(f'{"MÊS DO ANO":^120}')
print('-='*60)

mes=int(input('Informe o mês [1 a 12]:\n'))

match mes:
    case 1: 
        print('O mês informado é JANEIRO')
    case 2: 
        print('O mês informado é FEVEREIRO')
    case 3: 
        print('O mês informado é MARÇO')
    case 4: 
        print('O mês informado é ABRIL')
    case 5: 
        print('O mês informado é MAIO')
    case 6: 
        print('O mês informado é JUNHO')
    case 7: 
        print('O mês informado é JULHO')
    case 8: 
        print('O mês informado é AGOSTO')
    case 9: 
        print('O mês informado é SETEMBRO')
    case 10: 
        print('O mês informado é OUTUBRO')
    case 11: 
        print('O mês informado é NOVEMBRO')
    case 12: 
        print('O mês informado é DEZEMBRO')
    case _: 
        print('O mês informado é INVÁLIDO')