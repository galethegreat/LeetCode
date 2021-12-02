class Solution(object):
    def arrayPairSum(self, nums):
        
        sorted_nums = sorted(nums)
        length_of_nums = len(sorted_nums)

        if length_of_nums == 1:
            return sorted_nums[0]*2

        first_pointer = 0
        second_pointer = 1
        pairings = list()

        while second_pointer <= length_of_nums - 1:
            pairings.append(min(sorted_nums[first_pointer],sorted_nums[second_pointer]))
            first_pointer += 2
            second_pointer += 2

        Sum = sum(pairings)

        return Sum



def main():
    user_input = [2,2,2,2]
    print(Solution().arrayPairSum(user_input))
    #print(user_input)

if __name__ == "__main__":
    main()
