'''
numero1 = 5
numero2 = 3
print('Operador maior')
print(numero1 > numero2)
print(numero2 > numero1)
print('')
print('Operador menor')
print(numero1 < numero2)
print(numero2 < numero1)
idade = int(input('Informe sua idade: \n'))
if idade > 120:
    print('Você está morto!')
elif idade > 17:
    print(f'Você é maior de idade e possui {idade} anos')
elif idade <= 0:
    print('Você ainda não nasceu')
else:
    print(f'Você é menor de idade e possui {idade} anos')
'''
print('')
print('-='*60)
print(f'{"SESSÃO DE CINEMA":^120}')
print('-='*60)

'''
idade = int(input('Informe a sua idade: \n'))
if idade >= 18:
    print('Pode assistir o filme')
elif idade >= 16:
    acompanhado = input('Está companhado de adulto [S/N]?\n').strip().upper()
    if acompanhado == 'S':
        print('Pode assistir')
    else:
        print('Não pode assistir')
else:
    print('Não pode assistir')


idade = int(input('Informe a sua idade: \n'))
if idade < 18:
    acompanhado = input('Está acompnhado [S/N]?\n').strip().upper()
    if acompanhado == 'S':
        print('Pode assistir')
    else:
        print('Não pode assistir')
else: 
    print('Pode assistir')
'''
aladdin = input('Aladdin apareceu [S/N]?\n').strip().upper()
jasmine = input('Jasmine apareceu [S/N]?\n').strip().upper()

if aladdin == 'S' and jasmine == 'S':
    print('Love a noite inteira')
else:
    print('Não rolou o encontro')

print('<< OR >>')

if aladdin == 'S' or jasmine == 'S':
    print('Aproveitou que estava na rua e foi para a balada')
else:
    print('Não rolou o encontro')

print('<< NOT >>')
if not (aladdin == 'S' or jasmine == 'S'):
    print('Aproveitou que estava na rua e foi para a balada')
else:
    print('Não rolou o encontro')

