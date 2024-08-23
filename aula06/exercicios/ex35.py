# Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a multiplicação deles é igual a 20.
numeros = []
for i in range(2):
    numero = int(input(f'Informe {i+1}° número:\n'))
    numeros.append(numero)

if numeros[0] * numeros[1] == 20:
    print(f'A multiplicação de {numeros[0]} * {numeros[1]} é igual a 20')
else:
    print(f'A multiplicação de {numeros[0]} * {numeros[1]} é diferente de 20')
    
