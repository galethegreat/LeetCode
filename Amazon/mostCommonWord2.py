import string

class Solution(object):
    def mostCommonWord(self, paragraph, banned):

        banned_set = set(banned)
        punctions = set(['!','?',';','.',',',"'"])

        word_count = dict()

        exclude = set(string.punctuation)
        paragraph_without_punc = list()

        for character in paragraph.lower():
            if character not in exclude:
                paragraph_without_punc.append(character)
            else:
                paragraph_without_punc.append(" ")

        paragraph_without_punc = ''.join(paragraph_without_punc)
        words_in_paragraph = paragraph_without_punc.split()

        for word in words_in_paragraph:
            if word not in banned_set:
                word_count[word] = word_count.get(word, 0) + 1

        max_word = None
        max_count = None

        for word, count in word_count.items():

            if max_count is None or count > max_count:
                max_count = count
                max_word = word

        #max_list = list()
        #max_list=sorted([(count, word) for word, count in word_count.items()], reverse=True)

        return max_word

paragraph  = "Bob hit    a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
x = Solution().mostCommonWord(paragraph,banned)
print(x)
