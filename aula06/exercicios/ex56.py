# Escreva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e utilize um laço while para exibir a mensagem a quantidade de vezes desejada.
mensagem = str(input('Digite a mensagen:\n'))
repete = int(input('Informe quantas vezes você quer que a mensagem seja repetida [0 para sair]:\n'))
contador = 0
print('-='*60)
while contador < repete:
    print(mensagem)
    contador += 1

print('-='*60)
print('FIM DA EXECUÇÃO')
print('-='*60)


    
