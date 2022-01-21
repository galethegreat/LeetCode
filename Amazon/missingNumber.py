class Solution(object):
    def missingNumber(self, nums):
        #Space: O(n) Time: O(n)
        # largest = None
        # numbers_seen = set(nums)
        #
        #
        # for n in range(largest+1):
        #     if n in numbers_seen: continue
        #     else: return n
        #
        # return len(nums)

        #Space: O(1) Time: O(n)
        largest = None
        total = 0
        sum = 0
        if 0 not in nums: return 0
        for num in nums:
            if largest is None or num > largest:
                largest = num
            total += num

        for n in range(largest+1):
            sum += n
        if sum - total == 0:
            return len(nums)

        return sum - total

def main():

    nums = [0]
    print(Solution().missingNumber(nums))

if __name__ == "__main__":
    main()
