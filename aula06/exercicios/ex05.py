# Faça um programa que solicite ao usuário dois números e verifique se ambos são pares.

print('-='*60)
print(f'{'PAR OU ÍMPAR':^120}')
print('-='*60)

numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
if numero1 % 2 == 0 and numero2 % 2 == 0:
    print(f'{numero1} e {numero2} são PARES')
elif numero1 % 2 == 0 and numero2 % 2 != 0:
    print(f'{numero1} é PAR e {numero2} é ÍMPAR')
elif numero1 % 2 != 0 and numero2 % 2 == 0:
    print(f'{numero1} é ÍMPAR e {numero2} é PAR')
else:
    print(f'{numero1} e {numero2} são ÍMPARES')

print('-='*60)
print(f'{'FIM DO PROGRAMA':^120}')
print('-='*60)
