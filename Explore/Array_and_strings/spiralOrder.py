class Solution(object):
    def spiralOrder(self, matrix):

        number_of_rows = len(matrix)
        number_of_columns = len(matrix[0])

        if not number_of_columns or number_of_columns == 0:
            return []

        number_of_elements = number_of_rows * number_of_columns
        last_row = number_of_rows - 1
        last_column = number_of_columns - 1

        answer = list()

        right_traverse = True

        element = 0
        row = 0
        column = 0

        left_column_visited = -1
        top_row_visited = 0
        right_column_visited = number_of_columns
        bottom_row_visited = number_of_rows

        while element < number_of_elements:
            if right_traverse:

                while column < right_column_visited -1 and element <= number_of_elements:
                    answer.append(matrix[row][column])
                    element += 1
                    column += 1

                if element >= number_of_elements:break

                answer.append(matrix[row][column])
                element += 1
                row +=1
                right_column_visited = column

                while row < bottom_row_visited - 1 and element <= number_of_elements:
                        answer.append(matrix[row][column])
                        element += 1
                        row += 1

                if element >= number_of_elements:break

                bottom_row_visited = row
                answer.append(matrix[row][column])
                element += 1
                column -= 1

            else:

                while column > left_column_visited + 1 and element <= number_of_elements:
                    answer.append(matrix[row][column])
                    element += 1
                    column -= 1

                if element >= number_of_elements:break

                answer.append(matrix[row][column])
                element += 1
                row -= 1
                left_column_visited = column

                while row > top_row_visited +1 and element <= number_of_elements:
                    answer.append(matrix[row][column])
                    element += 1
                    row -= 1

                if element >= number_of_elements:break

                answer.append(matrix[row][column])
                element += 1
                top_row_visited = row
                column += 1


            right_traverse = not right_traverse

        return answer


#matrix = [[1,2,3,4,5],[]]
