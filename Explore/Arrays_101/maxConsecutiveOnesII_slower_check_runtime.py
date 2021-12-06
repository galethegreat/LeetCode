class Solution(object):

    def findMaxConsecutiveOnes(self, nums):

        if len(nums) == 1:
            return 1
        # if 1 not in nums:
        #     return 1
        count = 0
        zero_flag = 0
        p1 = None
        p2 = 0
        current_max = 0

        while p2 < len(nums):
            if nums[p2] == 0 and zero_flag == 0:
                count += 1
                zero_flag += 1
                p1 = p2
                p2 += 1

            elif nums[p2] == 1 :
                count += 1
                p2 += 1

            else:
                p2 = p1
                zero_flag = 0
                count = 0
                p2 += 1

            if count > current_max :
                current_max = count


        return current_max
