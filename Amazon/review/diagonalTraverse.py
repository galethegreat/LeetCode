class Solution(object):
    def findDiagonalOrder(self, matrix):
        num_of_rows = len(matrix)
        answer = list()

        for row in range(num_of_rows):
            row_temp = row
            col = 0
            while row_temp >= 0 :
                if col < len(matrix[row_temp]):
                    answer.append(matrix[row_temp][col])
                col += 1
                row_temp -= 1
        row_temp = row
        for col in range(1,len(matrix[row])):

            row_temp = row
            while row_temp >= 0 :
                if col < len(matrix[row_temp]):
                    answer.append(matrix[row_temp][col])
                col += 1
                row_temp -= 1


        return answer



def main():

    matrix = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    print(Solution().findDiagonalOrder(matrix))

if __name__== "__main__":
    main()
