class TicTacToe:

    def __init__(self, n: int):

        self.size = n

        self.diagonal = 0
        self.anti_diagonal = 0

        self.rows  = [0] * n
        self.cols = [0] * n

    def move(self, row: int, col: int, player: int) -> int:

        count = 1 if player == 1 else -1
        n = self.size
        if row == col:
            self.diagonal += count

        if col == self.size - 1 - row:
            self.anti_diagonal += count

        self.rows[row] += count

        self.cols[col] += count

        return player if (abs(self.diagonal) == n  or abs(self.anti_diagonal) == n or abs(self.rows[row]) == n or abs(self.cols[col]) == n) else 0
