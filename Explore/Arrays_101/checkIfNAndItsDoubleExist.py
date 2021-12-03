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
        #arr_squared = list()
        flag_0 = 0

        for number in arr_sorted:# n
            if number == 0:
                flag_0 += 1
                if flag_0 == 2: return True

            #arr_squared.append(number*2)

        for number in arr_sorted: #n
            if number == 0:continue

            if self.binarySearch(number*2,arr_sorted,0,len(arr_sorted)-1): #logn
                return True

        return False




nums1 = [0,0]
end = (len(nums1)-1)

print(Solution().checkIfExist(nums1))
