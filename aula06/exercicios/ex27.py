# Crie um programa que solicite ao usuário três números e exiba o maior deles.

print()
numero1 = int(input('Escolha um número:\n'))
numero2 = int(input('Escolha outro número:\n'))
numero3 = int(input('Escolha mais um número:\n'))

if numero1 > numero2 and numero1 > numero3:
    print(f'O maior núemro é {numero1}')
elif numero2 > numero1 and numero2 > numero3:
    print(f'O maior número é {numero2}')
elif numero3 > numero1 and numero3 > numero2:
    print(f'O maior número {numero3}')
else:
    print(f'Os números {numero1}, {numero2} e {numero3} são iguais')