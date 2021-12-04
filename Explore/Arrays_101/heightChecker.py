class Solution(object):
    def heightChecker(self, nums):
        #this is Time: O(nlog(n)), there is a O(n) solution with
        #count sort/using hash map
        if len(nums) == 1:
            return 0

        sorted_nums = sorted(nums)
        errors = 0

        for index in range(len(nums)):
            if sorted_nums[index] != nums[index]:
                errors += 1


        return errors

def main():
    nums = [1,2,3,4,5]
    print(Solution().heightChecker(nums))

if __name__ == "__main__":
    main()
