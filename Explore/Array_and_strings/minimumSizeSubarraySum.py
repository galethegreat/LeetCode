class Solution(object):
    def minSubArrayLen(self, target, nums):

        length_nums = len(nums)

        if length_nums == 1:
            if nums[0] == target:
                return 1
            return 0

        for num in nums:
            if num >= target:
                return 1

        first_pointer = 0
        second_pointer = 1
        total = nums[first_pointer]
        min_distance = float('inf')

        while second_pointer < length_nums:

            if total + nums[second_pointer] < target:

                total = total + nums[second_pointer]
                second_pointer += 1

            elif total + nums[second_pointer] >= target:

                distance = second_pointer- first_pointer + 1
                if distance == 2:
                    return 2

                elif distance < min_distance:
                    min_distance = distance
                total = total - nums[first_pointer]
                first_pointer += 1

        if min_distance != float('inf'):
            return min_distance
        else:
            return 0


def main():
    nums =  [1,4,4]
    target = 8
    print(Solution().minSubArrayLen(target,nums))


if __name__ == "__main__":
    main()
