# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
#
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.
# Example 1:
#
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
# Example 2:
#
# Input: paragraph = "a.", banned = []
# Output: "a"
#
#
# Constraints:
#
# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.

import string

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        dict_of_words = {}
        exclude = set(string.punctuation)
        #===============================================================
        characters_in_paragraph = list()
        for ch in paragraph.lower():
            if ch not in exclude:
                characters_in_paragraph.append(ch)
            else:
                characters_in_paragraph.append(' ')
        paragraph_without_punc = "".join(characters_in_paragraph)
        #===================================================================
        words_in_paragraph = paragraph_without_punc.split()

        for word in words_in_paragraph:
            if word not in banned:
                dict_of_words[word] = dict_of_words.get(word,0)+1
        max_words = sorted([(value,key) for key, value in dict_of_words.items()],reverse = True)

        max_word = max_words[0][1]

        return max_word

str_in = "a, a, a, a, b,b,b, c, c,"
banned = ["a"]
#this case tripped me up,the last one... it would not see b,b,b, because the way I did the join fucntion was to
#reject the letter if it was in exluded. The original way I did the part in the code I commented the block around
# was in simple :
#exclude = set(string.punctuation)
#paragraph_without_punc = ''.join(ch for ch in paragraph if ch not in exclude)
#but this would then return the above test case as "a a a a bbb c c" and thus bbb would be a word and not individual
x = Solution().mostCommonWord(str_in,banned)
print(x)
