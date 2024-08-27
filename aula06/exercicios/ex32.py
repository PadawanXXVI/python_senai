# pular esta

frase = str(input('Digite uma frase:\n')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print(f'O inverso {junto} é {inverso}')
if inverso == junto:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
