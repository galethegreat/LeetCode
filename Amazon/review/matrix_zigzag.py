class Solution(object):
    def findDiagonalOrder(self, matrix):
        num_of_rows = len(matrix)
        num_of_cols = len(matrix[0])
        if num_of_rows == 1:return matrix[0]
        if num_of_cols == 1: return [matrix[row][0] for row in range(num_of_rows)]
        answer = list()
        isUp = True
        row = 0
        col = 0
        i = 0
        while i < num_of_rows*num_of_cols:
            if isUp:
                while row >= 0 and col < num_of_cols:
                    answer.append(matrix[row][col])
                    i += 1
                    row -= 1
                    col += 1
                isUp = False
                if col >= num_of_cols:
                     col -= 1
                     row += 2
                else: row += 1

            else:
                while row < num_of_rows and col >= 0:
                    answer.append(matrix[row][col])
                    i += 1
                    row += 1
                    col -= 1
                isUp = True
                col += 1
                if row >= num_of_rows:
                    row -= 1
                    col += 1

        return answer



def main():

    matrix =  [[1,2,3],[4,5,6]]
    print(Solution().findDiagonalOrder(matrix))

if __name__== "__main__":
    main()
