# Métodos de String

texto = 'anderson de Matos Guimarães'

# CAPITALIZE
texto2 = texto.capitalize()
print(texto.capitalize())
print(texto2)
print('-='*40)

# UPPER
nome = 'aNDERson de mAToS guimaRÃES'
nome2 = nome.upper()
print(nome.upper())
print(nome2)
print('-='*40)

# LOWER
nome3 = nome.lower()
print(nome.lower())
print(nome3)
print('-='*40)

# REPLACE
silvanoSales = 'coração'
silvanoSales2 = silvanoSales.replace('ç','c').replace('ã','a')
print(silvanoSales.replace('çã','ca'))
print(silvanoSales2)
print('-='*40)

# STRIP - remove caracteres em branco no início e no fim de uma string
jackStripador = '      removendo espaços de uma string        '
print(jackStripador)
print(jackStripador.strip())
print('-='*40)

# SPLIT - transforma cada palavra em um elemento de uma lista

nomeEspalhado = 'Anderson de Matos Guimarães'
print(nomeEspalhado)
print(nomeEspalhado.split())
print('-='*40)

# JOIN - transforma os elementos uma lista em uma string única, ou seja, concatena strings
nomeLista = ['Anderson', 'de', 'Matos', 'Guimarães']
print(' '.join(nomeLista))
print('$'.join(nomeLista))

dominio = '@aluno.senai.br'

#print('anderson.m.guimaraes'.join(dominio))  -- verificar erro

# SLICE - manipula string por índice

cidade = 'Recanto das Emas, Cidade do Povo'
print(cidade[5:])
print(cidade[:13])
print(cidade[12:16])
print(cidade[:-1])
print(cidade[::-1])

palindromo = 'a torre da derrota'
palindromo2 = palindromo.strip()
if palindromo == palindromo[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')

if palindromo == palindromo2:
    print('É palíndromo')
else:
    print('Não é palíndromo')


