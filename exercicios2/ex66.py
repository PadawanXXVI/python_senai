'''
Escreva um algoritmo que forneça um menu para o usuário:
1 - Cadastrar nome,
2 - atualizar o nome,
3 - excluir,
4 - listar todos os cadastrados.
Ao final da operação deve dar uma mensagem indicando o resultado da operação e perguntando se deseja realizar outra operação, o seu aplicativo apenas deve encerrar quando a opção não for inserida.
'''

#Criando o menu:
def mostrar_menu():
    print('-='*20)
    print(f'{"Menu":^40}')
    print('1 - Cadastrar nome')
    print('2 - Atualizar nome')
    print('3 - Excluir')
    print('4 - Listar todos os cadastrados')
    print('0 - Sair do programa')
    print('-='*20)


def cadastrar_nome(nomes):
    nome = input('Digite o nome a ser cadastrado:\n')
    nomes.append(nome)
    print(f'Nome {nome} cadastrado com sucesso!')


def atualizar_nome(nomes):
    nome_antigo = input('Informe o nome a ser atualizado:\n')
    if nome_antigo in nomes:
        nome_novo = input('Digite o novo nome:\n')
        index = nomes.index(nome_antigo)
        nomes[index] = nome_novo
        print(f'Nome {nome_antigo} atualizado para {nome_novo} com sucesso!')
    else:
        print(f'Nome {nome_antigo} não localizado!')


def excluir_nome(nomes):
    nome = input('Digite o nome a ser excluído:\n')
    if nome in nomes:
        nomes.remove(nome)
        print(f'Nome {nome} excluído com sucesso!')
    else:
        print(f'Nome {nome} não localizado!')



def listar_nomes(nomes):
    if nomes:
        print('Nomes Cadastrados:')
        for nome in nomes:
            print(f'- {nome}')
    else:
        print('Nenhum nome cadastrado.')


def main():
    nomes = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_nome(nomes)
        elif opcao == '2':
            atualizar_nome(nomes)
        elif opcao == '3':
            excluir_nome(nomes)
        elif opcao == '4':
            listar_nomes(nomes)
        elif opcao == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
