def mostrar_tabuleiro(tabuleiro):
    print("\n+---+---+---+")
    for linha in tabuleiro:
        print("| {} | {} | {} |".format(*linha))
        print("+---+---+---+")

def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or \
           all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    # Verificar diagonais
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or \
       all([tabuleiro[i][2 - i] == jogador for i in range(3)]):
        return True
    return False

def jogar():
    # Inicializa tabuleiro com números
    tabuleiro = [[str(i + j * 3) for i in range(3)] for j in range(3)]
    jogador_atual = "X"
    jogadas = 0

    while True:
        mostrar_tabuleiro(tabuleiro)
        print(f"\nVez do jogador {jogador_atual}")

        try:
            posicao = int(input("Escolha uma célula (0–8): "))
            if posicao < 0 or posicao > 8:
                print("⚠️ Célula inválida.")
                continue
            linha, coluna = divmod(posicao, 3)
            if tabuleiro[linha][coluna] in ["X", "O"]:
                print("⛔ Célula ocupada.")
                continue
        except ValueError:
            print("❌ Entrada inválida.")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1

        if verificar_vencedor(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)
            print(f"\n🏆 Jogador {jogador_atual} venceu!")
            break
        elif jogadas == 9:
            mostrar_tabuleiro(tabuleiro)
            print("\n🤝 Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

# Inicia o jogo
jogar()