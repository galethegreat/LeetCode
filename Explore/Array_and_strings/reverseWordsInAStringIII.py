class Solution(object):

    def reverseWords(self, s):

        words = s.split()
        reversed_words = list()

        for word in words:
            # word_as_list = list(word)
            # word_as_list.reverse()
            # reversed_word = "".join(word_as_list)
            # reversed_words.append(reversed_word)
            reversed_words.append(word[::-1])

        return " ".join(reversed_words)
        #return " ".join([i[::-1] for i in s.split()]) 300 IQ one liner

user_input = "God Ding"

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
