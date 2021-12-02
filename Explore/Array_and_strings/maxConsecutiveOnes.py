class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        length_nums = len(nums)

        if length_nums == 1:
            return nums[0]

        if 1 in nums :
            max_distance = 1
        else:
            return 0

        first_pointer = 0
        second_pointer = 1

        while second_pointer < length_nums:
            if nums[first_pointer] == 1 and nums[second_pointer] == 1:
                if (second_pointer - first_pointer) + 1 > max_distance:
                    max_distance = second_pointer - first_pointer + 1
                second_pointer += 1
            else:
                first_pointer = second_pointer
                second_pointer += 1



        return max_distance


def main():
    nums = [1,0,1,1,1,0,1,1,1,1,0]

    print(Solution().findMaxConsecutiveOnes(nums))


if __name__ == "__main__":
    main()
