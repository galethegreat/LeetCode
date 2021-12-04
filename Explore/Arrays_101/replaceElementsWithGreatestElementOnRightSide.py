class Solution(object):
    def replaceElements(self, nums):

        if len(nums) == 1: return [-1]

        index =  len(nums) - 1

        current_largest = nums[index]

        index -= 1

        while index >= 0:

            if nums[index] < current_largest:

                nums[index] = current_largest

            else:
                over_write = current_largest
                current_largest = nums[index]
                nums[index] = over_write

            index -= 1

        nums[-1] = -1
        return nums



nums = [17,18,5,4,6,7]

print(Solution().replaceElements(nums))
#print(nums)
