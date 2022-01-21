class Solution:
    def twoSum(self, nums, target):

        complimentary_nums = dict()

        for position, number in enumerate(nums):
            if complimentary_nums.get((target-number), False):continue
            complimentary_nums[target-number] = position

        for index, number in enumerate(nums):
            position_complimentary = complimentary_nums.get(number, False)
            if position_complimentary and position_complimentary != index:
                return [index, position_complimentary]



def main():
    nums = [3,3,7,-5]
    target = 2
    print(Solution().twoSum(nums,target))

if __name__ == "__main__":
    main()
