nomes = []

def menu():    
    opcoes = ['Cadastrar nome', 'Atualizar nome', 'Excluir nome', 'Listar todos os cadastrados']

    print('-='*40)
    print(f'{"MENU":^40}')

    for indice, opcao in enumerate(opcoes):
        print(f'{indice + 1} - {opcao}')
    
    print('-='*40)

def listar_nomes():
    for indice, nome in enumerate(nomes):
        print(f'{indice} - {nome}')

def cadastrar_nome(nome):
    nomes.append(nome)


def atualiza_nome(nome, novo_nome):
    nomes[nomes.index(nome)] = novo_nome


def excluir_nome(nome):
    nomes.remove(nome)