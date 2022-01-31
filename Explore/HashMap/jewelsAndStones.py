class Solution(object):

    def isValidSudoku(self, board):

        rows = len(board)
        columns = len(board[0])
        for row in range(rows):
            elements = set()
            for column in range(columns):
                if board[row][column] == '.':continue
                if board[row][column] in elements:return False
                elements.add(board[row][column])

        for column in range(columns):
            elements = set()
            for row in range(rows):
                if board[row][column] == '.':continue
                if board[row][column] in elements:return False
                elements.add(board[row][column])

        bounds = [[0,3],[3,6],[6,9]]
        for bound in bounds:
            elements = set()
            elements_2 = set()
            elements_3 = set()
            for row in range(bound[0],bound[1]):

                    for column in range(0,3):
                        if board[row][column] == '.':continue
                        if board[row][column] in elements:return False
                        elements.add(board[row][column])

                    for column_2 in range(3,6):
                        if board[row][column_2] == '.':continue
                        if board[row][column_2] in elements_2:return False
                        elements_2.add(board[row][column_2])

                    for column_3 in range(6,9):
                        if board[row][column_3] == '.':continue
                        if board[row][column_3] in elements_3:return False
                        elements_3.add(board[row][column_3])

        return True

def main():
    board = [[".",".",".",".","5",".",".","1","."],
             [".","4",".","3",".",".",".",".","."],
             [".",".",".",".",".","3",".",".","1"],
             ["8",".",".",".",".",".",".","2","."],
             [".",".","2",".","7",".",".",".","."],
             [".","1","5",".",".",".",".",".","."],
             [".",".",".",".",".","2",".",".","."],
             [".","2",".","9",".",".",".",".","."],
             [".",".","4",".",".",".",".",".","."]]

    print(Solution().isValidSudoku(board))

if __name__ == "__main__":
    main()
