class Solution(object):
    def isToeplitzMatrix(self, matrix):
        num_of_rows = len(matrix)
        num_of_col  = len(matrix[0])
        if num_of_col == 1 or num_of_rows == 1: return True

        for col in range(num_of_col):
            diagonal_value = matrix[0][col]
            for row in range(num_of_rows):
                if matrix[row][col] != diagonal_value: return False
                col += 1
                if col >= num_of_col: break

        for row in range(1, num_of_rows):
            diagonal_value = matrix[row][0]
            for col in range(num_of_col):
                if matrix[row][col] != diagonal_value: return False
                row += 1
                if row >= num_of_rows: break

        return True



def main():

    matrix = [[1,2],[2,2]]
    print(Solution().isToeplitzMatrix(matrix))

if __name__== "__main__":
    main()
