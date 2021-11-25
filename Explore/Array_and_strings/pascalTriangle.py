class Solution(object):
    def generate(self, numRows):
        
        if numRows == 1 :
            return [[1]]

        answer = [[1]]
        answer_row = list()

        for row in range(1,numRows):
            answer_row.append(answer[row-1][0])
            index = 1
            while index < row:
                answer_row.append(answer[row-1][index] + answer[row-1][index-1])
                index += 1

            answer_row.append(answer[row-1][row-1])

            answer.append(answer_row)
            answer_row = []

        return answer

x = Solution().generate(5)
print(x)
#Input: numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
#1 5 10 10 1

#1 1 1 1 1
#1 2 3 4
#1 3 6 10
#1 4 10
#1 5
#Input: numRows = 1
#Output: [[1]]
