# Desenvolva um algoritmo que pergunte ao usuário o nome de uma cidade e verifique se é a capital do Brasil.
print()
cidade = str(input('Digite o nome de uma cidade brasileira:\n')).lower()

if cidade == 'brasília':
    print(f'{cidade} é a capital do Brasil.')
else:
    print(f'{cidade} não é a capital do Brasil.')

