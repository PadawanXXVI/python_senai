# Crie um programa que solicite ao usuário dois números e exiba a soma, subtração, multiplicação e divisão entre eles.

print('-='*60)
print(f'{"OPERAÇÕES BÁSICAS":^120}')
print('-='*60)

numero1 = int(input('Escolha um número:\n'))
numero2 = int(input('Escolha outro número:\n'))
soma = numero1 + numero2
subt = numero1 - numero2
multi = numero1 * numero2
divi = numero1 / numero2
print(f'A soma de {numero1} e {numero2} é {soma}')
print(f'A subtração de {numero1} e {numero2} é {subt}')
print(f'A multiplicação de {numero1} e {numero2} é {multi}')
print(f'A divisão de {numero1} e {numero2} é {divi}')

print('-='*60)
print(f'{"FIM DO PROGRAMA":^120}')
print('-='*60)

