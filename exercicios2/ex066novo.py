nomes = []
operacao = 'sim'

while operacao == 'sim':
    print('1 - Cadastrar nome')
    print('2 - Atualizar nome')
    print('3 - Excluir nome')
    print('4 - Lsitar nomes')
    opcao = int(input('Informe a ação desejada:\n'))

    match opcao:
        case 1:
            nome = input('Que nome deseja cadastrar?\n')
            nomes.append(nome)
        case 2:
            nome = input('Que nome deseja atualizar?\n')
            novo_nome = input('Qual será o novo nome?\n')
            nomes[nomes.index(nome)] = novo_nome
        case 3:
            nome = input('Que nome deseja remover?\n')
            nomes.remove(nome)
        case 4:
            for indice, nome in enumerate(nomes):
               print(f'{indice} - {nome}')
        case _:
            print('Opção inválida')

    operacao = input('Deseja realizar outra operação [sim / nao]?\n').strip().lower()

    if operacao == 'nao':
        print(f'{"<<< FIM DA EXECUÇÃO >>>":^40}')
        break