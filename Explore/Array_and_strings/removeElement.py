class Solution(object):
    def removeElement(self, nums, val):

#Two Pointer Technique:
        original_length = len(nums)

        index_to_copy_to = 0
        for index_to_check in range(original_length):
            if nums[index_to_check] != val:
                nums[index_to_copy_to] = nums[index_to_check]
                index_to_copy_to += 1

        #Do not get confused, returning how many elements to print in nums
        #so the grader will look at nums[0:index_to_copy_to+1]
        return index_to_copy_to

# Maybe more intutative solution:
        # original_length = len(nums)
        # if original_length  == 0:
        #     return 0
        # if original_length == 1:
        #     if nums[0] == val:
        #         return 0
        #     return 1
        #
        # index = 0
        # while index < len(nums):
        #     if nums[index] == val:
        #         nums.pop(index)
        #         continue
        #
        #     index += 1
        #
        # return len(nums)


def main():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(Solution().removeElement(nums,val))
    print(nums)

if __name__ == "__main__":
    main()
