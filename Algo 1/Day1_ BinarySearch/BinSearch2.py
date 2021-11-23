def isBadVersion(num):
    bad = 5
    num_is_bad = False
    
    if(num >= bad):
        num_is_bad = True
    
    return num_is_bad


class Solution:

    def firstBadVersion(self, n):
        version_bad = None
        low = 1
        high = n+1
        guess = 1
       
        if (isBadVersion(guess)):
            version_bad = guess
           
        
        else:
            guess = low + (high-low)//2
        
                
            while high - low > 1:
                guess = low + (high-low)//2
                
                    
                if (isBadVersion(guess)):
                    high = guess
                    version_bad = guess                    
    
                else:
                    low = guess
            
        return version_bad


h = Solution.firstBadVersion(Solution,5)
print(h)
