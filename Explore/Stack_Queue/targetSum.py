class Solution:
    def findTargetSumWays(self, nums, target):
        cache = dict()

        def backtrack(index, total):

            if index == len(nums):
                return 1 if total == target else 0

            if (index,total) in cache:
                return cache[(index,total)]

            cache[(index,total)] = (backtrack(index+1, total + nums[index]) + backtrack(index+1, total - nums[index]))

            return cache[(index,total)]
        return backtrack(0,0)

target = 3
nums =  [1,1,1,1,1]

print(Solution().findTargetSumWays(nums,target))
