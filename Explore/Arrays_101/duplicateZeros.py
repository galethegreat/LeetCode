class Solution(object):
    def duplicateZeros(self, nums):

        if len(nums) == 1:
            if nums[0] == 0:
                return [0,0]
            else:
                return nums

        index = 0
        last_element_index = len(nums) - 1
        flag = 0
        while index <= last_element_index:
            if nums[index] == 0:
                if index == last_element_index:
                    index +=1
                    flag = 1
                    break
                last_element_index -= 1
            index += 1

        pointer = index-1
        last = len(nums) - 1

        if nums[pointer] == 0 and flag :
            nums[last] = 0
            pointer -= 1
            last -= 1
        while pointer >= 0:
            if nums[pointer] != 0:
                nums[last] = nums[pointer]
                pointer -= 1
                last -= 1
            else:
                nums[last] = 0
                nums[last-1] = 0
                last -= 2
                pointer -= 1


user_input = [1,0,2,3,0,4,5,0]
print(Solution().duplicateZeros(user_input))
print(user_input)
