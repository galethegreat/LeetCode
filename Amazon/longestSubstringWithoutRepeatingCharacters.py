class Solution:
    def lengthOfLongestSubstring(self, s):

        if len(s) <= 1: return len(s)

        current_largest = 0
        current_largest_substring = None
        current_substring = set()
        substring = list()
        p1 = 0
        for p2, letter in enumerate(s):
            if letter not in current_substring:
                current_substring.add(letter)

            else:
                if len(current_substring) > current_largest:
                    current_largest = len(current_substring)
                    current_largest_substring = (p1, p2)

                while letter in current_substring:
                    current_substring.remove(s[p1])
                    p1 += 1
                current_substring.add(letter)


        if len(current_substring) > current_largest:
            current_largest = len(current_substring)
            current_largest_substring = (p1,p2+1)

        return current_largest
        #return (s[current_largest_substring[0]:current_largest_substring[1]])

def main():
    s = "dvdf"
    #    01234567

    print((Solution().lengthOfLongestSubstring(s)))

if __name__ == "__main__":
    main()
