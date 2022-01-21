class Solution:
    def diagonalSum(self, mat):
        if len(mat) == 1: return mat[0][0]

        num_of_rows = len(mat)
        num_of_col = len(mat[0])

        sum = 0
        for row in range(num_of_rows):
            sum += mat[row][row]

        col = num_of_col-1
        row = 0
        for row in range(num_of_rows):
            if row != col:
                sum  += mat[row][col]
            col -= 1

        return sum

def main():
    matrix  = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().diagonalSum(matrix))
if __name__ == "__main__":
    main()
