class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        if len(nums) == 1:
            return nums[0]

        first = 0
        second = 0
        max_distance = 0

        while second < len(nums):
            if nums[first] == 1 and nums[second] == 1:

                distance = second - first +1

                if distance > max_distance:
                    max_distance = distance
                second += 1
            else:
                first = second
                first += 1
                second += 1

        return max_distance
        
user_input = [1,0,1,1,0,1]
print(Solution().findMaxConsecutiveOnes(user_input))
