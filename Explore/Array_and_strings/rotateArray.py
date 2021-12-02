class Solution(object):
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        len_of_nums = len(nums)
        if len_of_nums == 1: return None

        if k > len_of_nums:  ##bruh this optimization rekt me on acceptance rate
            real_number_of_rotations = k % (len_of_nums)
        else:
            real_number_of_rotations = k

        while real_number_of_rotations > 0:

            nums.insert(0, nums.pop(-1))

            real_number_of_rotations -= 1

        #could also 300 IQ it like this:
        # s = k % len(nums)
        #nums[:] = nums[-s:] + nums[:-s]

def main():
    nums =  [1,2]
    k = 2
    Solution().rotate(nums,k)
    print (nums)


if __name__ == "__main__":
    main()
