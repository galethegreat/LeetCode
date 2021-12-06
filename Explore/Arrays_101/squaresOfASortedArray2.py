class Solution(object):

    def sortedSquares(self, nums):

        if len(nums) == 1:
            return [nums[0]*nums[0]]

        answer = list()

        p1 = 0
        p2 = len(nums) -1

        while p2 >= p1: 

            num1 = nums[p1]*nums[p1]
            num2 = nums[p2]*nums[p2]

            if num1 >= num2 :
                answer.append(num1)
                p1 += 1

            else:
                answer.append(num2)
                p2 -= 1

        answer.reverse() #On

        return answer


def main():
    nums = [-10]

    print(Solution().sortedSquares(nums))

if __name__ == "__main__":
    main()
