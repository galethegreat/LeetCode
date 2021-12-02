class Solution(object):
    def reverseWords(self, s):
        strip_s = s.split()
        strip_s.reverse()

        return " ".join(strip_s)

user_input = "Alice does not even like bob"

x = Solution().reverseWords(user_input)
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
