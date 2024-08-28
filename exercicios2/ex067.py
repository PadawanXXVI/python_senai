# Desenvolve um jogo da velha desenvolvido em python que funcione no terminal


def imprimir_tabuleiro(tabuleiro):
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

def verificar_vencedor(tabuleiro, jogador):
    condicoes_vitoria = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    for condicao in condicoes_vitoria:
        if all(tabuleiro[i] == jogador for i in condicao):
            return True
    return False

def jogo_da_velha():
    tabuleiro = [str(i) for i in range(1, 10)]
    jogador_atual = "X"
    jogadas = 0

    while jogadas < 9:
        imprimir_tabuleiro(tabuleiro)
        jogada = int(input(f"Jogador {jogador_atual}, escolha um campo (1-9): ")) - 1

        if tabuleiro[jogada] in "XO":
            print("Campo já preenchido. Tente novamente.")
            continue

        tabuleiro[jogada] = jogador_atual
        jogadas += 1

        if verificar_vencedor(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            return

        jogador_atual = "O" if jogador_atual == "X" else "X"

    imprimir_tabuleiro(tabuleiro)
    print("Empate!")

if __name__ == "__main__":
    jogo_da_velha()
