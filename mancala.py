class Mancala:
    PLAYER_ONE_MANCALA = 6
    PLAYER_TWO_MANCALA = 13

    #INICIA A CLASSE COM O TABULEIRO COM 4 PEDRAS EM CADA POÇO E JÁ OS DOS JOGADORES VAZIOS
    def __init__(self):
        self.board = [4] * 14
        self.board[self.PLAYER_ONE_MANCALA] = 0
        self.board[self.PLAYER_TWO_MANCALA] = 0
    #INTERFACE DO TABULEIRO
    def displayBoard(self):
        print("\n" + "-" * 39)
        print("|    | 12 | 11 | 10 |  9 |  8 |  7 |    |")
        print("|----|----|----|----|----|----|----|----|")
        print(f"|    | {self.board[12]:2} | {self.board[11]:2} | {self.board[10]:2} | {self.board[9]:2} | {self.board[8]:2} | {self.board[7]:2} |    |")
        print(f"| {self.board[13]:2} |----|----|----|----|----|----| {self.board[6]:2} |")
        print("|    |  0 |  1 |  2 |  3 |  4 |  5 |    |")
        print("-" * 39)

    def gameOver(self):
        return all(piece == 0 for piece in self.board[1:6]) or all(piece == 0 for piece in self.board[8:13])
    
    """
    FUNÇÃO PRINCIPAL ONDE REALIZA O MOVIMENTO COM BASE NO JOGADOR ATUAL E FAZ A DISTRIBUIÇÃO E CAPTURA DAS PEDRAS
    É UTILIZADO UMA LÓGICA DE VERIFICAÇÃO ONDE PEGA O INDÍCE DO POÇO E COMPARA COM O QUE FOI COLOCADO PELO JOGADOR
    """
    def makeMove(self, pit):
        if self.board[pit] == 0:
            print("MOVIMENTO INVÁLIDO. O POÇO ESTÁ VAZIO")
            return False

        stones = self.board[pit]
        self.board[pit] = 0

        pit = self.distributeStones(pit, stones)

        if pit == self.PLAYER_ONE_MANCALA:
            return True

        if self.board[pit] == 1 and self.board[12 - pit] > 0 and pit < 6:
            self.captureStones(pit)
        return pit == self.PLAYER_ONE_MANCALA
    
    def captureStones(self, pit):
        self.board[self.PLAYER_ONE_MANCALA] += self.board[pit] + self.board[12 - pit]
        self.board[pit] = self.board[12 - pit] = 0

    def distributeStones(self, start_pit, stones):
        pit = start_pit
        while stones > 0:
            pit = (pit + 1) % 14
            if pit != self.PLAYER_TWO_MANCALA:
                self.board[pit] += 1
                stones -= 1
        return pit

    def play(self):
        current_player = 0

        while not self.gameOver():
            self.displayBoard()
            if current_player == 0:
                print("TURNO DO JOGADOR 1 (PARTE INFERIOR DA TELA)")
            else:
                print("TURNO DO JOGADOR 2 (PARTE SUPERIOR DA TELA)")

            try:
                pit = int(input("ESCOLHA UM POÇO (0-5): ")) + current_player * 7
                if not (0 <= pit <= 5 + current_player * 7):
                    raise ValueError
                if self.makeMove(pit):
                    current_player = (current_player + 1) % 2
            except ValueError:
                print("MOVIMENTO INVÁLIDO. VOCÊ SÓ PODE IR DE 0-5")

        self.displayBoard()
        print("O JOGO ACABOU!")
        if self.board[self.PLAYER_ONE_MANCALA] > self.board[self.PLAYER_TWO_MANCALA]:
            print("JOGADOR 1 GANHOU!")
        elif self.board[self.PLAYER_ONE_MANCALA] < self.board[self.PLAYER_TWO_MANCALA]:
            print("JOGADOR 2 GANHOU!")
        else:
            print("DEU EMPATE, EITA!!")


if __name__ == "__main__":
    game = Mancala()
    game.play()
