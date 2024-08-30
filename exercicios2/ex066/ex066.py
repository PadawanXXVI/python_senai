'''
Escreva um algoritmo que forneça um menu para o usuário:
1 - Cadastrar nome,
2 - atualizar o nome,
3 - excluir,
4 - listar todos os cadastrados.
Ao final da operação deve dar uma mensagem indicando o resultado da operação e perguntando se deseja realizar outra operação, o seu aplicativo apenas deve encerrar quando a opção não for inserida.
'''
from os import system
import operacoes as op
# from operacoes import menu, listar_nomes
# import operacoes

operacao = 'sim'

while operacao == 'sim':
    op.menu()
    opcao = int(input('Informe a operação desejada:\n'))
    
    match opcao:
        case 1:
            nome = input('Que nome deseja cadastrar?\n')

            op.cadastrar_nome(nome)
        case 2:
            nome = input('Que nome deseja atualizar?\n')
            novo_nome = input('Qual será o novo nome?\n')
            
            op.atualiza_nome(nome, novo_nome)
        case 3:
            nome = input('Que nome deseja remover?\n')
            
            op.excluir_nome(nome)
        case 4:
            op.listar_nomes()
        case _:
            print('Opção inválida')

    operacao = input('Deseja realizar outra operação [sim / nao]?\n').strip().lower()
    system('clear')

    if operacao != 'sim':
        break
