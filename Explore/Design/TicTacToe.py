class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for row in range(n)]

    def move(self, row: int, col: int, player: int) -> int:

        self.board[row][col] = player if player == 2 else - 1

        return self.checkBoard(self.board)

    def checkBoard(self, board):

        size_of_board = len(board)

        #check rows if player 1 or 2 has filled it out fully
        for row in board:

            if sum(row) == -1 * size_of_board:
                return 1
            elif sum(row) == 2 * size_of_board:
                return 2

        #check each col if player 1 or 2 has filled it out fully
        for col in range(len(board)):

            col_sum = 0
            for row in range(len(board[0])):
                col_sum += board[row][col]

            if col_sum == -1 * size_of_board:
                return 1
            elif col_sum == 2 * size_of_board:
                return 2

        #check diagonal
        diagonal_sum = 0
        for row in range(len(board)):
            diagonal_sum += board[row][row]

        if diagonal_sum == -1 * size_of_board:
            return 1
        elif diagonal_sum == 2 * size_of_board:
            return 2

        #check anti diagonal
        anti_diagonal_sum = 0
        for row in range(len(board)):
            anti_diagonal_sum += board[row][len(board[0]) - 1 - row]

        if anti_diagonal_sum == -1 * size_of_board:
            return 1

        elif anti_diagonal_sum == 2 * size_of_board:
            return 2

        return 0
        
