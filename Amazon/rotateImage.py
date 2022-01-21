class Solution(object):

    def rotate(self, matrix):

        m = len(matrix)
        n = len(matrix[0])
        index_start = 0

        for row in range(m):

            for column in range(index_start,n):
                if row == column: continue
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]

            index_start += 1

        for row in range(m):
            p1 = 0
            p2 = len(matrix[0]) - 1
            while p1 < p2:
                matrix[row][p1],matrix[row][p2] = matrix[row][p2], matrix[row][p1]
                p1 += 1
                p2 -= 1

def main():

    matrix =[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

    Solution().rotate(matrix)
    print(matrix)
if __name__ == "__main__":
    main()
