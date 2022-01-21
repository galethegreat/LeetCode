class Solution(object):

    def strStr(self, haystack, needle):
        if len(needle) == 0: return 0
        if len(haystack) == 0: return -1

        for index, char in enumerate(haystack):
            if char == needle[0]:
                if haystack[index:(index+len(needle))] == needle:
                    return index

        return -1

        #return haystack.find(needle) one liner solution but the above is just practice


def main():
    haystack = "hello"
    needle = "ll"
    print(Solution().strStr(haystack, needle))

if __name__ == "__main__":
    main()
