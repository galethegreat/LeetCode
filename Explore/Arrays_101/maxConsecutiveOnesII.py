class Solution(object):

    def findMaxConsecutiveOnes(self, nums):

        if len(nums) == 1:
            return 1
        if 1 not in nums:
            return 1
        count = 0
        zero_flag = 0
        p1 = 0
        p2 = 0
        current_max = 0

        while p2 < len(nums):

            if nums[p2] == 0 and zero_flag == 0:
                count += 1
                zero_flag += 1

                p2 += 1

            elif nums[p2] == 1 :
                count += 1
                p2 += 1

            else:
                while zero_flag == 1:
                    if nums[p1] == 0:
                        zero_flag -= 1
                        count -= 1

                    else:
                        count -= 1
                    p1 += 1

            if count > current_max :
                current_max = count

        return current_max

def main():
    nums = [0,1,1,0,1,1,1,0,0]

    print(Solution().findMaxConsecutiveOnes(nums))

if __name__ == "__main__":
    main()
