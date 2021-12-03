class Solution(object):

    def binarySearch(self,number,nums,start,stop):
        if len(nums) == 0:
            return False
        if start >= len(nums) or stop == 0:
            return False
        if start == stop:
            return nums[start] == number


        midpoint = (start+stop)//2

        if nums[midpoint] == number:return True

        elif nums[midpoint] < number:

            start = midpoint+1
            return self.binarySearch(number,nums,start,stop)

        else:

            stop = midpoint
            return self.binarySearch(number,nums,start,stop)

    def checkIfExist(self, arr):


        arr_sorted= sorted(arr) #nlog(n)
        flag_0 = 0

        for number in arr_sorted:# n
            if number == 0:  # checks if 0 is present multiple times
                flag_0 += 1 #[0,1,2,3,] returns false
                if flag_0 == 2: return True #but [0,0,1,2,3,] returns true


        for number in arr_sorted: #n
            if number == 0:continue #skips 0 to avoid false postive

            if self.binarySearch(number*2,arr_sorted,0,len(arr_sorted)-1): #logn
                return True

        return False




nums1 = [0,0]
end = (len(nums1)-1)

print(Solution().checkIfExist(nums1))
