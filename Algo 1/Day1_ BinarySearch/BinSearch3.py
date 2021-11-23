


class Solution:

    def searchInsert(self, nums, target):
        index = None
        length_of_nums = len(nums)
        low = 0
        high = length_of_nums
        guess = 0
       
        if (nums[guess]==target):
            
            index = guess
    
        elif (nums[guess] < target and high ==1):
            index = 1
        else:
            guess = low + (high-low)//2
        
                
            while low <= high:
                guess = low + (high-low)//2
              
                    
                if ( guess < length_of_nums and nums[guess] > target  ):
                    high = guess -1    
                    index = guess               
    
                elif  guess < length_of_nums and nums[guess] == target:
                    index = guess
                    break
                elif guess >= length_of_nums:
                    index = length_of_nums
                    break
                else:
                    low = guess +1
               
                if high - low == 1 and nums[guess] < target:
                    
                    index = guess + 1
               
              
                    
                elif high - low == 1 :
                    
                    index = guess

            
        return index
    
nums = [-1,3,5,6]
target = 0

h = Solution.searchInsert(Solution,nums,target)
print(h)
