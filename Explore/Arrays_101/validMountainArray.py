class Solution(object):

    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False
        if arr[0] >= arr[1]:
            return False
        previous = -1
        direction_up = True
    
        for number in arr:
        #    print(f"{number} {previous} {direction_up}")
            if direction_up:
                if previous == number:
                    return False
                elif previous < number:
                    previous = number
                else:
                    direction_up = False
                    previous = number
            else:
                if previous == number:
                    return False
                elif previous > number:
                    previous = number
                else:
                    return False
        if direction_up:
            return False
        else:
            return True





nums1 =[0,1,2,3,4,5,6,7,8,9]
end = (len(nums1)-1)

print(Solution().validMountainArray(nums1))
