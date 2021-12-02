class Solution(object):
    def strStr(self, haystack, needle):

        number_of_characters_in_needle = len(needle)
        number_of_characters_in_haystack = len(haystack)

        if number_of_characters_in_needle == 0:
            return 0

        if number_of_characters_in_haystack == 0:
            return -1

        if number_of_characters_in_haystack < number_of_characters_in_needle:
            return -1

        needle_position_in_haystack = -1

        for index_haystack,character_haystack in enumerate(haystack):
            if (number_of_characters_in_haystack - index_haystack) < number_of_characters_in_needle: break

            if character_haystack == needle[0]:

                start_index = index_haystack
                end_index = start_index + number_of_characters_in_needle

                haystack_sub_string = haystack[start_index:end_index]
                if haystack_sub_string == needle:
                    needle_position_in_haystack = index_haystack
                    break



        return needle_position_in_haystack

        #if index > number_of_characters_in_haystack:

        #needle_position = haystack.find(needle) can be done with this one liner
        #practcing just to impliment the find() method myself above, first tried
        #double for loops, but then realized I can directly check if strings are the same
        #using ==

        #return needle_position

haystack = "hello"
needle =   "a"
x = Solution().strStr(haystack,needle)
print(x)
