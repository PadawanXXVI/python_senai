# Desenvolva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e depois use um for para imprimir essa mensagem repetidas vezes.
mensagem = str(input("Digite a mensagem:\n"))
iteracao = int(input("Informe quantas vezes você quer imprimir a mensagem:\n"))
for i in range(iteracao):
    print(mensagem)
    