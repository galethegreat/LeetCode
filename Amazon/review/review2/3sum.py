class Solution(object):
    def twoSum(self, nums, target, avoid_index):

        compliment = dict()
        answer = list()

        for index, num in enumerate(nums):
            if index == avoid_index: continue
            compliment[target - num] = index

        for index, num in enumerate(nums):
            if index == avoid_index: continue

            if compliment.get(num, False) and compliment[num] != index:
                answer.append([nums[index], nums[compliment[num]]])

        return answer

    def threeSum(self, nums):
        if len(nums) <= 2: return []

        answers = list()
        answers_no_duplicates = set()
        nums_tested = set()

        for index, num in enumerate(nums):
            if num in nums_tested:continue
            nums_tested.add(num)

            two_sum_lists = self.twoSum(nums, -num, index)

            for two_sum in two_sum_lists:

                two_sum.append(num)
                two_sum.sort()
                temp_toup = (two_sum[0], two_sum[1], two_sum[2])

                if temp_toup not in answers_no_duplicates:
                    answers.append(two_sum)
                    answers_no_duplicates.add(temp_toup)

        return answers

def main():
    nums = [-1,0,1,2,-1,-4]
    print(Solution().threeSum(nums))

if __name__ == "__main__":
    main()
