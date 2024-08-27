# Escreva um programa que solicite ao usuário para digitar dois números e verifique se o primeiro é maior que o segundo. Continue pedindo números até que o primeiro número seja maior que o segundo.
while True:
    numero1 = int(input('Informe o primeiro número:\n'))
    numero2 = int(input('Informe o segundo número:\n'))
    if numero1 > numero2:
        print(f'O primeiro número {numero1} é maior que o segundo número {numero2}')
        print('FIM DA EXECUÇÃO')
        break
    else:
        print(f'O primeiro númerp {numero1} é menor que o segundo número {numero2}')
        print('Tente novamente!')
    