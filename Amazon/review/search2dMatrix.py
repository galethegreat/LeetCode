class Solution(object):
    def searchMatrix(self, matrix, target):
        def binSearchRow(low,high,target,matrix):
            start_row = (high-low) // 2 + low

            if matrix[start_row][0] == target:return start_row
            elif matrix[start_row][0] > target:
                if start_row - 1 < 0:return False
                elif matrix[start_row-1][0] <= target:return start_row-1
                high = start_row
                return binSearchRow(low,high,target,matrix)
            elif matrix[start_row][0] < target:
                if start_row + 1 >= len(matrix) :return start_row
                elif matrix[start_row+1][0] > target:return start_row
                low = start_row
                return binSearchRow(low,high,target,matrix)

        def binSearch(low,high,row, target):

            if low > high : return False
            element_index = (high-low)//2 + low
            if element_index >= len(row):return False
            if row[element_index] == target:return True
            elif row[element_index] < target:
                low = element_index+1
                return binSearch(low,high,row, target)
            elif row[element_index] > target:
                high = element_index-1
                return binSearch(low,high,row, target)

        num_of_rows = len(matrix)
        num_of_cols =  len(matrix[0])
        start_row = binSearchRow(0,len(matrix),target,matrix)

        if start_row is False: return False
        elif matrix[start_row][0] == target: return True
        else:
            row = matrix[start_row]
            low = 0
            high = len(row)-1

            return binSearch(low,high,row,target)



def main():

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(Solution().searchMatrix(matrix,target))

if __name__== "__main__":
    main()
