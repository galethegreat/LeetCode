class Solution(object):
    def productExceptSelf(self, nums):

        #Space: O(n)
        # answer_left = [1]
        # answer_right = [1]
        # for index in range(1, len(nums)):
        #     answer_left.append(nums[index-1]*answer_left[-1])
        #
        # for reverse_index in range(len(nums)-2,-1,-1):
        #     answer_right.append(answer_right[-1]*nums[reverse_index+1])
        #
        # answer_right.reverse()
        # answer = list()
        # for num_left, num_right in zip(answer_left, answer_right):
        #     answer.append(num_left * num_right)

        #Space: O(1) not cointing the answer array for some reason idk why
        answer= [1]
        for index in range(1,len(nums)):
            answer.append(nums[index-1]*answer[index-1])

        right_most = 1

        for reverse_index in range(len(nums)-1, -1, -1):
            answer[reverse_index] = right_most * answer[reverse_index]
            right_most = right_most*nums[reverse_index]

        return answer

def main():

    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))

if __name__ == "__main__":
    main()
