class Solution(object):
    def sortArrayByParity(self, nums):
        p1 = 0
        p2 = len(nums) - 1

        while p1 < len(nums) and p1 < p2:

            while nums[p2] % 2 != 0 and p1 < p2:
                p2 -= 1

            if p1 >= p2:break

            if nums[p1] % 2 == 0:
                p1 += 1

            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
                p1 += 1

        return nums


        #Time: O(n)  Space: O(n)
        # odd = list()
        # even = list()
        # answer = list()
        #
        # for num in nums:
        #     if num % 2 == 0 :
        #         even.append(num)
        #     else:
        #         odd.append(num)
        #
        # answer = even + odd
        #
        # return answer

def main():
    nums = [1,1,1,3,3,5,5,7]
    print(Solution().sortArrayByParity(nums))

if __name__ == "__main__":
    main()
