class Queen(object):
    def __init__(self, val, n):
        self.position = None
        self.val = val
        self.n_board = n
        self.prev = None


    def setCoordinate(self, new_coordinate):
        coordinate = new_coordinate
        self.position = coordinate


    def getCoordinate(self):
        position = self.position
        return position

    def updateCoordinate(self):
        self.prev = self.getCoordinate()
        if self.position is None:
            self.position = [0, 0]
            return True
        else:
            if self.position[0] < self.n_board-1:
                 self.position[0] += 1
                 return True

            elif self.position[1] < self.n_board-1:
                self.position[0] = 0
                self.position[1] += 1
                return True

            else:
                self.position = None
                return False

    def reverseCoordinate(self):
        prev = self.prev
        self.setCoordinate(prev)

class Solution():
    def __init__(self):
        self.queen_positions = dict()
        self.board_coordinates= dict()
        self.queen = 0
        self.num_of_queens = 0
        self.board = None
        self.visited = set()

    def attackedSquares(self, queen):
        rows, cols = len(self.board), len(self.board[0])

        queen_coordinate = queen.getCoordinate()

        x, y = queen_coordinate[0], queen_coordinate[1]

        self.board_coordinates[queen.val] = set()
        self.board_coordinates[queen.val].add((x,y))
        for row in range(rows): self.board_coordinates[queen.val].add((x, row))
        for col in range(cols): self.board_coordinates[queen.val].add((col, y))

        x_diagonal, y_diagonal = x, y
        while x_diagonal < rows and y_diagonal < cols:
            self.board_coordinates[queen.val].add((x_diagonal, y_diagonal))
            x_diagonal += 1
            y_diagonal += 1

        x_diagonal, y_diagonal = x, y
        while x_diagonal >= 0 and y_diagonal < cols:
            self.board_coordinates[queen.val].add((x_diagonal, y_diagonal))
            x_diagonal -= 1
            y_diagonal += 1

        x_diagonal, y_diagonal = x, y
        while x_diagonal >= 0 and y_diagonal >= 0:
            self.board_coordinates[queen.val].add((x_diagonal, y_diagonal))
            x_diagonal -= 1
            y_diagonal -= 1

        x_diagonal, y_diagonal = x, y
        while x_diagonal < rows and y_diagonal >= 0:
            self.board_coordinates[queen.val].add((x_diagonal, y_diagonal))
            x_diagonal += 1
            y_diagonal -= 1

    def canPlaceQueen(self, queen, queens):

        coordinates = (queen.getCoordinate()[0], queen.getCoordinate()[1])
        for queen_placed in range(queens):
            coordinates_attacked = self.board_coordinates.get(queen_placed, [])
            if coordinates in coordinates_attacked: return False

        return True


    def solveNQueens(self, n):
        if n <= 3: self.num_of_queens = 1
        if n == 3: self.num_of_queens = 2
        if n > 3: self.num_of_queens = n

        self.board = [[ '.' for _ in range(n)] for _ in range(n)]
        rows, cols = len(self.board), len(self.board [0])

        queens = [Queen(queen_val, n) for queen_val in range(self.num_of_queens)]

        queens.reverse()
        start_queen = queens[-1]
        start_queen_position = start_queen.getCoordinate()
        placed_queens = list()
        answers = list()

    #    while start_queen.position is None or start_queen.position[0] < n - 2:
        while start_queen.updateCoordinate():

            if (start_queen.position[0],start_queen.position[1]) in self.visited:continue
            print(self.visited)
            print(start_queen.position)
            print(start_queen.prev)
            start_queen.reverseCoordinate()
            print(start_queen.position)

            self.board = [[ '.' for _ in range(n)] for _ in range(n)]
            rows, cols = len(self.board), len(self.board [0])
            while queens:
                current_queen = queens.pop()
                queenPlaced = False

                while current_queen.updateCoordinate():
                    if self.canPlaceQueen(current_queen, self.num_of_queens):
                        self.attackedSquares(current_queen)
                        placed_queens.append(current_queen)
                        queenPlaced = True
                        break

                if not queenPlaced:
                    self.board_coordinates[placed_queens[-1].val] = set()
                    last_queen = placed_queens.pop()
                    queens.append(current_queen)
                    queens.append(last_queen)

            while placed_queens:
                placed_queen = placed_queens.pop()

                coordinate = (placed_queen.position[0], placed_queen.position[1])
                self.board[coordinate[0]][coordinate[1]] = 'Q'
                self.visited.add(coordinate)
                if placed_queen != start_queen:
                    placed_queen.position = None
                else:
                    start_queen_position = placed_queen.getCoordinate()
                queens.append(placed_queen)

            joined_board = list()
            for row in self.board:
                joined_board.append("".join(row))
            print(joined_board)
            print(start_queen_position)
            print(start_queen.position)
            print()
            answers.append(joined_board)

            self.board_coordinates = dict()

        return(answers)

def main():

    n = 4

    print(Solution().solveNQueens(n))

if __name__ == "__main__":
    main()
