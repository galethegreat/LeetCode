class Solution(object):
    def spiralOrder(self, matrix):

        num_of_rows = len(matrix)
        num_of_cols = len(matrix[0])
        number_of_elements = num_of_rows*num_of_cols
        visited = set()
        answer = list()
        row = 0
        col = 0

        while len(visited) < number_of_elements:
            while col < num_of_cols:
                if (row,col) not in visited:
                    answer.append(matrx[row][col])
                    visited.add((row,col))
                else:
                    col-=1
                    break
                col += 1
            while row < num_of_rows:
                if (row,col) not in visited:
                    answer.append(matrx[row][col])
                    visited.add((row,col))
                else:
                    row-=1
                    break
                row += 1
            while col >= 0:
                if (row,col) not in visited:
                    answer.append(matrx[row][col])
                    visited.add((row,col))
                else:
                    col +=1
                    break
                col -= 1
            while row >= 0:
                if (row,col) not in visited:
                    answer.append(matrx[row][col])
                    visited.add((row,col))
                else:
                    row +=1
                    break
                row -= 1

        return answer



def main():

    matrix =  [[1,2,3],[4,5,6]]
    print(Solution().spiralOrder(matrix))

if __name__== "__main__":
    main()
