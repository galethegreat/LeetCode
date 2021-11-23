# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 19:48:32 2021

@author: Gale
"""
class Solution:
    def sortedSquares(self, nums):
        nums_squared = []
        for element in nums:
            nums_squared.append( element**2 ) 
       
        
        nums_squared.sort()
        
        return nums_squared
        
        
nums = [-7]

test = Solution.sortedSquares(Solution,nums)
print(test)