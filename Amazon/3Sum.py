class Solution:
    def threeSum(self, nums):
        def twoSum(nums, target,avoid_index):
            answer = set()
            complimentary_nums = dict()
            for index,num in enumerate(nums):
                if index == avoid_index:continue
                complimentary_nums[target-num] = index
            for index, num in enumerate(nums):
                if index == avoid_index:continue
                if complimentary_nums.get(num, False):
                    if nums[complimentary_nums.get(num)] != num:
                        if (nums[index], nums[complimentary_nums.get(num)]) in answer:continue
                        answer.add((nums[complimentary_nums.get(num)], nums[index] ))
            return answer

        answer_list = list()
        answer_set = set()
        if len(nums) <= 2: return []

        isAllZeros = True
        numOfZeroes = 0
        for num in nums:
            if num != 0:
                isAllZeros = False
            else:
                numOfZeroes += 1

        if isAllZeros: return [[0,0,0]]
        if numOfZeroes >= 3: answer_list.append([0,0,0])

        for index, num in enumerate(nums):

            answer = twoSum(nums,-num,index)

            if len(answer) > 0:
                for ans in answer:
                    if (ans[0],ans[1],num) in answer_set or (ans[0],num,ans[1]) in answer_set or (num,ans[0],ans[1]) in answer_set or (ans[1],ans[0],num) in answer_set or (ans[1],num,ans[0])in answer_set or (num,ans[1],ans[0]) in answer_set: continue
                    answer_list.append([ans[0],ans[1],num])
                    answer_set.add((ans[0],ans[1],num))


        return answer_list

def main():

    nums  = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    print((Solution().threeSum(nums)))

if __name__ == "__main__":
    main()
