from collections import deque
class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):

        def wordValidTransform(word_one, word_two):

            allowed_error = 1
            errors = 0

            for index in range(len(word_one)):
                if word_one[index] == word_two[index]:continue
                else: errors += 1
                if errors > allowed_error: return False

            return True

        if endWord not in wordList: return 0

        q = deque()
        q.append(beginWord)
        level = 0
        while q:
            q_size = len(q)
            k = 0
            level += 1
            while k < q_size:
                current_word = q.popleft()
                k += 1
                if current_word == endWord: return level
                for index in range(len(wordList) - 1, -1, -1):
                    if wordList[index] == current_word:
                        wordList.pop(index)
                        continue
                    if wordValidTransform(current_word, wordList[index]):
                        q.append(wordList[index])
                        wordList.pop(index)

        return 0

def main():
    beginWord = 'hot'
    endWord = 'dot'
    wordList = ["hot","dot","dog"]
    print(Solution().ladderLength(beginWord, endWord, wordList))

if __name__ == "__main__":
    main()
