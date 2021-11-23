class Solution(object):


    def piviotIndex(self,nums):

        left_sum = 0
        Sum = sum(nums)


        if len(nums) == 1:
            return 0

        else:
            for index, number in enumerate(nums):

                right_sum = Sum - left_sum - number

                if(left_sum == right_sum ):
                    return index

                left_sum += number
            return -1



x = Solution().piviotIndex([-1,-7,-3,6,5,6])
print(x)


#nums = [1,7,3,6,5,6]
#nums = [1,2,3]
#nums = [2,1,-1]
#nums = [-1,-7,-3,6,5,6]
