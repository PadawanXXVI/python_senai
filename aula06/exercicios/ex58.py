# Desenvolva um algoritmo que solicite ao usuário uma palavra e continue pedindo outra palavra até que ele digite "sair".

while True:
    palavra = input('Informe a palavra [sair - para sair do prgrama]:\n').lower()
    if palavra == 'sair':
        print('FIM DA EXECUÇÃO')
    else:
        print('Digite outra palavra:\n')