# Faça um programa que peça ao usuário três números e verifique se todos são positivos.

print()

numero1 = int(input('Digite um número:\n'))
numero2 = int(input('Digite outro número:\n'))
numero3 = int(input('Digite mais um número:\n'))

if numero1 > 0 and numero2 > 0 and numero3 > 0:
    print('Os números são positivos')
elif numero1 == numero2 == numero3 == 0:
    print('Os números são iguais a 0 "zero"') 
else:
    print('Nem todos os números são positivos')
    
