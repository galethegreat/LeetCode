class Solution:

    def search(self, nums, target):
        index_of_target = -1

        if(len(nums) == 1):
            bin_search_guess = 0
            if (nums[bin_search_guess] == target):
                index_of_target = bin_search_guess
            else:
                index_of_target = -1
        else :
            bin_search_low = 0
            bin_search_high = len(nums)
            bin_search_guess = int((bin_search_high+bin_search_low )/2.0)
            while bin_search_guess > 0 and bin_search_guess < len(nums)  :


                bin_search_guess = int((bin_search_high+bin_search_low )/2.0)

                if bin_search_high - bin_search_low == 1:
                    if (nums[bin_search_guess] == target):
                        index_of_target = bin_search_guess

                    break
                if(nums[bin_search_guess] < target) :
                    bin_search_low = bin_search_guess


                elif(nums[bin_search_guess] > target):
                    bin_search_high = bin_search_guess
                


                if (nums[bin_search_guess] == target):
                    index_of_target = bin_search_guess

                    break

        return index_of_target


test =  [-1,0,3,5,9,12]

target = 13
h = Solution.search(Solution,test, target)
print(h)
