# Faça um programa que pergunte ao usuário a idade e verifique se ele pode votar (idade maior ou igual a 16).

print('-='*60)
print(f'{"MAIORIDADE ELEITORAL":^120}')
print('-='*60)

idade = int(input('Informe a idade do cidadão:\n'))

if idade < 16:
    print(f'O cidadão tem {idade} anos e NÃO PODE VOTAR')
elif 16 <= idade <= 65:
    print(f'O cidadão tem {idade} anos e o VOTO É ORBRIGATÓRIO')
else:
    print(f'O cidadão tem {idade} anos e o VOTO É OPCIONAL')

print('-='*60)
print(f'{"FIM DO PROGRAMA":^120}')
print('-='*60)
