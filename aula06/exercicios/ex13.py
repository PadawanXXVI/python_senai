# Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.

print('-='*60)
print(f'{"MÊS DO ANO":^120}')
print('-='*60)

mes = int(input('Escolha o mês correspondente de 1 a 12:\n'))

while mes not in range(1,13):
    print('O mês digitado é inválido')
    break
while mes in range(1,13):
    if 3 <= mes <= 5:
        print(f'O mês de {mes} é outono')
    elif 6 <= mes <= 8:
        print(f'O mês de {mes} é inverno')
    elif 9 <= mes <= 11:
        print(f'O mês de {mes} é primavera')
    else:
        print(f'O mês de {mes} é verão')
