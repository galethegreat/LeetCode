class Solution(object):
    def generateMatrix(self, matrix_size):

        num_of_rows = matrix_size
        num_of_cols = matrix_size
        number_of_elements = num_of_rows*num_of_cols
        visited = set()
        element_value = 1
        row = 0
        col = 0
        matrix = [[0]*num_of_cols for row in range(num_of_rows)]


        while len(visited) < number_of_elements:
            while col < num_of_cols:
                if (row,col) not in visited:
                    matrix[row][col] = element_value
                    visited.add((row,col))
                    element_value += 1
                else:
                    col -=1
                    row +=1
                    break
                col += 1
            if col >= num_of_cols:
                col -=1
                row +=1
            while row < num_of_rows:
                if (row,col) not in visited:
                    matrix[row][col] = element_value
                    visited.add((row,col))
                    element_value += 1
                else:
                    row -=1
                    col -= 1
                    break
                row += 1
            if row >= num_of_rows:
                row -=1
                col -=1
            while col >= 0:
                if (row,col) not in visited:
                    matrix[row][col] = element_value
                    visited.add((row,col))
                    element_value += 1
                else:
                    col +=1
                    row -=1
                    break
                col -= 1
            if col < 0:
                col +=1
                row -=1
            while row >= 0:
                if (row,col) not in visited:
                    matrix[row][col] = element_value
                    visited.add((row,col))
                    element_value += 1
                else:
                    row +=1
                    col+=1
                    break
                row -= 1
            if row < 0:
                row +=1
                col+=1
        return matrix



def main():

    matrix_size = 1
    print(Solution().generateMatrix(matrix_size))

if __name__== "__main__":
    main()
