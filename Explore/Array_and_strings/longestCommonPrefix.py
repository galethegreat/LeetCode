class Solution(object):
    def longestCommonPrefix(self, strs):

        if len(strs) == 1:
            return strs[0]

        smallest_string = None

        for word in strs:
            if len(word) == 0:
                return ""

            if smallest_string is None or len(word) < len(smallest_string):
                smallest_string = word

        found_prefix = False
        prefix_end_index = 0
        for index in range(len(smallest_string)):
            for word in strs:
                if smallest_string[0:index+1] == word[0:index+1]:
                    found_prefix = True
                else:
                    found_prefix = False
                    break

            if found_prefix:
                prefix_end_index = index +1
            else:
                break

        return smallest_string[0:prefix_end_index]
