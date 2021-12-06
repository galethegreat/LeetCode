class Solution(object):

    def thirdMax(self, nums):

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0],nums[1])

        max_list = [None,None,None]
        maximum = None
        count = 0

        while count < 3:
            for num in nums:
                if (maximum is None or num > maximum) and num != max_list[0] and num != max_list[1]:
                    maximum = num


            max_list[count] = maximum
            count += 1
            maximum = None

        if max_list[0] is not None and max_list[1] is not None and max_list[2] is not None:
            if max_list[0] > max_list[1] and max_list[1] > max_list[2]:
                return max_list[2]

            else:
                return max_list[0]
        else:
            return max_list[0]



def main():
    nums = [3,3,4,3,4,3,0,3,3]

    print(Solution().thirdMax(nums))

if __name__ == "__main__":
    main()
