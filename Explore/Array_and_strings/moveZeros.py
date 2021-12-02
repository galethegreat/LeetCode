class Solution(object):

    def moveZeroes(self, nums):

        if len(nums) <= 1:
            return None

        pointer = 0
        index = 0

        while index < len(nums):

            if nums[index] != 0:

                nums[pointer], nums[index] = nums[index] , nums[pointer]
                pointer += 1
                index +=1
            else:
                index += 1

        return None

# =======This solution below is O(n^2) because pop(i) is O(n) !!!!===================
        if len(nums) <= 1:
            return None
        first_pointer = 0
        second_pointer = len(nums) - 1

        while first_pointer < second_pointer :

            if nums[first_pointer] ==  0:

                nums.append(nums.pop(first_pointer))
                second_pointer -= 1
                continue

            else:
                first_pointer += 1
#=========================================================================================





user_input = [1,1,0,3,12]

x = Solution().moveZeroes(user_input)
print(user_input)
