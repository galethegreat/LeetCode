class Solution:
    def transpose(self, mat):
        num_of_rows = len(mat)
        num_of_col = len(mat[0])
        mat_transpose = [[0 for col in range(num_of_rows)] for row in range(num_of_col)]
        for col in range(num_of_col):
            for row in range(num_of_rows):
                mat_transpose[col][row] = mat[row][col]

        return mat_transpose


matrix = [[1,2,3],[4,5,6]]
print(Solution().transpose(matrix))
