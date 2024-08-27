# Forma tradicional de criar uma 'função' para somar dois números:
# numero1 = int(input('Informe o número: '))
# numero2 = int(input('Informe o número: '))

# print('A soma é: ', numero1+numero2)

numeros = [1, 5, 8, 10, 3, 78, 100, 51]


#Funções próprias
print(max(numeros))
print(min(numeros))
print(len(numeros))
print(len('Anderson'))
print(sum(numeros))

media = (sum(numeros) / len(numeros))

print(media)

# Ciração de uma função que recebe uma lista e calcula a média
def media(numeros):
    resultado = sum (numeros) / len(numeros)
    return resultado


print(media(numeros))


# Criação de uma função que recebe dois numeros e soma:
def soma (numero1, numero2):
    soma = numero1 + numero2
    return soma


#Uso da função soma
print(soma(15,35))


#Função sem return
def saudacao(nome):
    print(f'Oi, {nome}!') # o print já está dentro da função, por isso não precisa de 'return'

saudacao('Anderson')


# Criação de função com parâmetro opcional
def ola (nome, mensagem='Olá, '):
    print(mensagem , nome)

ola('Anderson', 'Bem-vindo, ')
ola('Anderson')


#Criando função com múltiplo 'return':

def dividir(numero1, numero2):
    resposta = numero1 // numero2
    resto = numero1 % numero2
    return resposta, resto



divisao = dividir(9, 2)

print(divisao)


'''
numero5 = int(input("Informe um número: "))
print(f'O número digitado é {numero5:.2f}')
print(type(numero5))
'''


# Função lambda
somar = lambda a, b: a + b

print(somar(10,5))


# Função com infinitos parâmetros
# ** Parâmetros não nomeados - ou posicionais


def exibir_informacoes(*args): # o parâmetro precisa ser chamado de 'args', mas não impede ter outro nome, gera uma tupla
    print('Argumentos posicionais: ', args)


exibir_informacoes(1, 4, 'Anderson', True)

# ** Parâmetros nomeados

def exibir_informacoes2(**args): # recebe múltiplos parâmetros, mas precisam ter um nome, gera um dicionário
    print('Argumentos nomeados: ', args)


exibir_informacoes2(nome='Anderson', idade=25, curso='python')

# Dicionários
'''
key: value
=
chave : valor

pessoa = {
    'nome': 'Anderson',
    'idade': 25,
    'estado_civil': 'solteiro',
    'escolaridade': 'bacharel'
}
'''

pessoas = [{
    'nome': 'Anderson',
    'idade': 25,
    'estado_civil': 'solteiro',
    'escolaridade': 'bacharel'
},
{
    'nome': 'Daniel',
    'idade': 19,
    'estado_civil': 'noivo',
    'escolaridade': 'superior'
}]
print()
print(pessoas)
print()
print('-='*40)
print(pessoas[1])
print()


