# Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.

print('-='*60)
print(f'{'OPERAÇÃO MATEMÁTICA'}')
print('-='*60)

numero1 = int(input('Escolha um número\n'))
numero2 = int(input('Escolha outro número:\n'))
soma = subt = multi = divi = 0
operacao = int(input('''
ESOLHA A OPERAÇÃO MATEMÁTICA ABAIXO:
      1 - SOMA
      2 - SUBTRAÇÃO
      3 - MULTIPLICAÇÃO
      4 - DIVISÃO
      '''))
if operacao == 1:
    soma = numero1 + numero2
    print(f'A soma de {numero1} e {numero2} é {soma}')
elif operacao == 2:
    subt = numero1 - numero2
    print(f'A subtração de {numero1} e {numero2} é {subt}')
elif operacao == 3:
    multi = numero1 * numero2
    print(f'A multiplicação entre {numero1} e {numero2} é {multi}')
elif operacao == 4:
    divi = numero1 / numero2
    print(f'A divisão de {numero1} por {numero2} é {divi}')
else:
    print('Valor da operação errado.')

print('-='*60)
print(f'{'FIM DE PROGRAMA':^120}')
print('-='*60)



    