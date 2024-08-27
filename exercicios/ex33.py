# Crie um programa que solicite ao usuário o valor de um produto e calcule o desconto de 10%.
produto = float(input('Informe o valor do produto:\n'))
desconto = produto * 0.1

print(f'O valor de desconto de 10% do produto é R$ {desconto}')
print(f'O valor do produto com desconto é R$ {produto-desconto}')
