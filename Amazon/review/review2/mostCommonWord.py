from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):

        punc = "!?',;."
        banned_set = set(banned)
        punc_set = set(punc)

        letters_no_punc = list()
        letters_in_paragraph = list(paragraph)

        for letter in letters_in_paragraph:
            if letter in punc_set:
                letters_no_punc.append(' ')
            else:
                letters_no_punc.append(letter)

        words_no_punc = "".join(letters_no_punc)
        words = words_no_punc.split()

        words_with_no_banned_words = list()
        for word in words:
            word_lowered = word.lower()
            if word_lowered in banned_set or word_lowered in punc_set:continue
            words_with_no_banned_words.append(word_lowered)

        words_and_count= Counter(words_with_no_banned_words)

        most_common_words = sorted([(count, word) for word, count in words_and_count.items()], reverse=True)

        return most_common_words[0][1]

def main():

    paragraph  = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(Solution().mostCommonWord(paragraph, banned))

if __name__ == "__main__":
    main()
