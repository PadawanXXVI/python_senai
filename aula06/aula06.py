from ast import match_case


print()
print('-='*60)
print(f'{"MATCH CASE":^120}')




'''
if candidato == 13:
    print('Votou no Lula')
elif candidato == 22:
    print('Votou no Bolsonaro')
else:
    print('Candidato inválido')
'''
'''

candidato = int(input('Informe o número do candidato:\n'))

match candidato:
    case 13:
        print('Votou no Molusco')
    case 22:
        print('Votou no Lunático')
    case _:
        print('Opção inválida')
'''

# ATRIBUIÇÃO DE VARIÁVEL

numero = 10
print(numero)

numero += 10
print(numero)

numero -= 10
print(numero)

numero *= 10
print(numero)

numero /= 10
print(numero)


# VERIFICANDO SE É PAR OU ÍMPAR
"""
if numero % 2 == 0:
    print("O número é par")
else:
    print('O número é ímpar')

"""

print('')
print(f'{"LAÇOS DE REPETIÇÃO":^120}')
print('')
'''
for i in range (5):
    print('Anderson')
    print(i)

nomes = ['Anderon','Lucas','Laura']

for pessoa in nomes:
    print(pessoa)
'''

# frutas = ['banana', 'maçã', 'morango', 'laranja']

# for fruta in frutas:
#     print(fruta)

# for indice, fruta in enumerate(frutas):
#     print(f'Suas frutas são {indice}: {fruta}')
"""
nomes = []

for i in range(5):
    nome = input(f'Informe o {i+1}º nome: ')
    nomes.append(nome)
print(nomes)

for nome in nomes:
    print(nome)
"""
'''
nome = 'Anderson'

for i in nome:
    print(i)

'''

print('')
print('-='*60)
print(f'{"WHILE - EM PORTUGUÊS SIGNIFICA *ENQUANTO* ":^120}')
'''
numero = None

while numero != 0:
    numero = int(input('Informe o número: '))
'''

contador = 1
numero = int(input('Informe um número: '))


while contador < 10:
    numero *= 2
    print(numero)
    contador += 1

