# Escreva um programa que peça ao usuário para inserir dois números e verifique se o primeiro é maior que o segundo.

print('-='*60)
numero1 = int(input("Informe um número:\n"))
numero2 = int(input('Informe outro número:\n'))

if numero1 == numero2:
    print(f'{numero1} e {numero2} são iguais')
elif numero1 > numero2:
    print(f'{numero1} é maior que {numero2}')
else:
    print(f'{numero1} é menor que {numero2}')