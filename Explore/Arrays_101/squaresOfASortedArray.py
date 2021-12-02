class Solution(object):
    def sortedSquares(self, nums):

        if len(nums) == 1:
            return [nums[0]**2]

        first = 0
        last = len(nums) - 1

        answer = list()

        while first <= last:
            if (nums[first])** 2 > (nums[last])**2:
                answer.append(nums[first]**2)
                first +=1
            else:
                answer.append(nums[last]**2)
                last -=1

        answer.reverse()

        return answer


user_input = [-7,-3,2,3,11]
print(Solution().sortedSquares(user_input))
