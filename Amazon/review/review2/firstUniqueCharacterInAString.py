from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        chars_and_freq = Counter(s)

        for index, char in enumerate(s):
            if chars_and_freq[char] == 1:
                return index

        return -1

def main():

    s = "loveleetcode"
    print(Solution().firstUniqChar(s))

if __name__ == "__main__":
    main()
