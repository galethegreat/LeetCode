class Solution():

    def search(self, nums, target):
        self.nums = nums
        self.target = target

        position = 0;
        position_of_target = None
        for num in self.nums:

            if num == self.target :
                if position_of_target is None:
                    position_of_target = position
            position += 1
        if position_of_target is None:
            position_of_target = -1

        print(position_of_target)



nums = [-1,0,3,5,9,12]
target = 9
test = Solution().search(nums,target)
