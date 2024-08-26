# Crie um algoritmo que peça ao usuário para digitar uma senha e verifique se a senha é "1234".

print()
print('-='*60)
print(f'{"VERIFICAÇÃO DE SENHA":^120}')
print('-='*60)

senha = str(input('Informe sua senha:\n'))

if senha == "1234":
    print(f'Você digitou a senha {senha}. Escolha outra!')
else:
    print('Senha cadastrada com sucesso!')

print('-='*60)
print(f'{"FIM DO PROGRAMA":^120}')
print('-='*60)
