class Solution:

    def threeSumClosest(self, nums,target):

        closest_answer = None
        nums.sort()

        for index in range(len(nums)):

            p1 = index + 1
            p2 = len(nums) - 1

            while p1 < len(nums) and p1 != p2:

                answer = nums[index] + nums[p1] + nums[p2]

                if closest_answer is None or abs(target - answer) < abs(target - closest_answer):
                     closest_answer = answer
                     if closest_answer == target: return closest_answer

                if answer < target:
                    p1 += 1
                else:
                    p2 -= 1

        return closest_answer

def main():

    nums  =  [0,0,0]
    target = 1
    print((Solution().threeSumClosest(nums, target)))

if __name__ == "__main__":
    main()
