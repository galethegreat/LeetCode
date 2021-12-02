class Solution(object):
    def getRow(self, rowIndex):

        if rowIndex == 0 :
            return [1]
        if rowIndex == 1:
            return [1,1]
        previous_row = [1,1]


        # there is a O(n) solution with math, come back later to figure it out
    
        for row in range(2,rowIndex+1):
            answer_row = []
            answer_row.append(previous_row[0])
            index = 1

            while index < len(previous_row):
                answer_row.append(previous_row[index]+previous_row[index-1])
                index += 1
            answer_row.append(previous_row[-1])
            previous_row = answer_row

        return answer_row





x = Solution().getRow(3)
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
