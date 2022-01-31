class Solution(object):
     def isIsomorphic(self, s, t):
        if len(s) == 1 and len(t) == 1: return True

        letters_in_s = dict()
        letters_in_t = dict()

        for letter_s, letter_t in zip(s, t):
            letters_in_s[letter_s] = letter_t
            letters_in_t[letter_t] = letter_s

        for letter_s, letter_t in zip(s, t):
            if letters_in_s[letter_s] != letter_t: return False
            if letters_in_t[letter_t] != letter_s: return False

        return True


def main():
    s = "paper"
    t = "title"
    print(Solution().isIsomorphic(s,t))

if __name__ == "__main__":
    main()
