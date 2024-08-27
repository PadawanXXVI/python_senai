# Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.

print('-='*60)
print(f'{"SISTEMA DE ESCOLHA DE CORES":^120}')
print('-='*60)

cor = int(input('Selecione uma cor: 1 - vermelho; 2 - verde; 3 - azul:\n'))
if cor == 1:
    print('A cor escolhida foi "vermelho"')
elif cor == 2:
    print('A cor escolhida foi "verde"')
elif cor == 3:
    print('A cor escolhida foi "azul"')
else:
    print('Número inválido')

print('-='*60)
print(f'{'FIM DO PROGRAMA':^120}')
print('-='*60)
