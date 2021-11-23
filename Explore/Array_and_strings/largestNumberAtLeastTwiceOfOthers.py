class Solution(object):

    def dominantIndex(self,nums):

        if len(nums) == 1:
            return 0
        else:
            largest_number = None
            index_of_largest_number = None
            for index, number in enumerate(nums):
                if(largest_number is None or number > largest_number):
                    largest_number = number
                    index_of_largest_number = index
            output = index_of_largest_number
            for index, number in enumerate(nums):
                if(index != index_of_largest_number and number*2 > largest_number):
                    output = -1
                    break
            return output
x = Solution().largestNumberAtLeastTwiceOfOthers(nums)
