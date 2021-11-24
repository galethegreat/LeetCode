class Solution(object):

    def findDiagonalOrder(self, matrix ):

        if not matrix or not matrix[0]:
            return []

        answer = list()

        number_of_rows = len(matrix)
        number_of_columns  = len(matrix[0])
        last_column = number_of_columns -1
        last_row = number_of_rows-1

        direction_is_up = True
        row = 0
        column = 0
        while row < number_of_rows and column < number_of_columns:
            if direction_is_up:
                while row > 0  and column < last_column :
                    answer.append(matrix[row][column])
                    row -= 1
                    column += 1
                answer.append(matrix[row][column])
                if(column == last_column):
                    row += 1
                else:
                    column += 1
            else:
                while column > 0  and row < last_row :
                    answer.append(matrix[row][column])
                    column -= 1
                    row += 1
                answer.append(matrix[row][column])
                if(row == last_row):
                    column += 1
                else:
                    row += 1

            direction_is_up = not(direction_is_up)

        return answer
