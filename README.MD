# JOGO MANCALA EM PYTHON
Mancala é um antigo jogo de tabuleiro que tem sido jogado há séculos em várias culturas ao redor do mundo. Existem muitas variações do jogo, com diferentes nomes e regras específicas, dependendo da região.
Este é um exemplo simples utilizando a linguagem python.

## Regras Básicas do Mancala:
### Tabuleiro
Tabuleiro com 2 filas de 6 poços e 2 Mancalas.
Os poços menores são para armazenar pedras.
As Mancalas são maiores e usadas para coletar pedras.
```python
def displayBoard(self):
        print("\n" + "-" * 39)
        print("|    | 12 | 11 | 10 |  9 |  8 |  7 |    |")
        print("|----|----|----|----|----|----|----|----|")
        print(f"|    | {self.board[12]:2} | {self.board[11]:2} | {self.board[10]:2} | {self.board[9]:2} | {self.board[8]:2} | {self.board[7]:2} |    |")
        print(f"| {self.board[13]:2} |----|----|----|----|----|----| {self.board[6]:2} |")
        print("|    |  0 |  1 |  2 |  3 |  4 |  5 |    |")
        print("-" * 39)
```


### Distribuição de Pedras:
Inicialmente, os poços (exceto as Mancalas) são preenchidos com um número igual de pedras.
```python
def distributeStones(self, start_pit, stones):
        pit = start_pit
        while stones > 0:
            pit = (pit + 1) % 14
            if pit != self.PLAYER_TWO_MANCALA:
                self.board[pit] += 1
                stones -= 1
        return pit
```
### Turnos
Os jogadores alternam os turnos.
Em um turno, o jogador escolhe um dos poços de sua fila.

### Movimento

O jogador retira todas as pedras do poço escolhido.
Ele distribui uma pedra em cada poço no sentido anti-horário, incluindo o seu, mas não a do oponente.
```python
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
```


### Captura

Se a última pedra cair na Mancala do jogador, ele joga novamente.
Se a última pedra cair em um poço vazio do jogador, ele captura as pedras do poço oposto e as coloca em sua Mancala.
```python
 def captureStones(self, pit):
        self.board[self.PLAYER_ONE_MANCALA] += self.board[pit] + self.board[12 - pit]
        self.board[pit] = self.board[12 - pit] = 0
```
### Fim do Jogo
O jogo termina quando todos os poços de um jogador estiverem vazios.
O jogador com mais pedras em sua Mancala vence.

### CASO TENHA ALGUM BUG POR FAVOR REPORTAR PARA UMA FUTURA MANUTENÇÃO
<img src="eu.jpeg" width="40%" margin="auto" alt="eu">