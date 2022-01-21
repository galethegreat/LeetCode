from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):

        if len(s) == 1: return 0

        count_lettrs = Counter(s)

        for index, letter in enumerate(s):
            if count_lettrs[letter] == 1:
                return index

        return -1

def main():

    s = "aabb"
    print(Solution().firstUniqChar(s))

if __name__ == "__main__":
    main()
