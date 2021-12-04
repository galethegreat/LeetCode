class Solution(object):
    def removeDuplicates(self, nums):

        if len(nums) <= 1:
            return 1

        p1 = 0
        p2 = 1
        p3 = 1

        while p2 < len(nums):
            if nums[p1] == nums[p2]:
                p2 += 1

            else:
                if p2 != p3:
                    nums[p3] = nums[p2]
                p3 += 1
                p1 = p2
                p2 += 1

        return p3

def main():
    nums =  [1,1]
    k = Solution().removeDuplicates(nums)
    print(nums[0:k])
if __name__ == "__main__":
    main()
