class Solution(object):
    def merge(self, nums1, m, nums2, n):

    #this solution uses O(n) space, but it runs O(n)
    #a simple tweek to this would be to use 2 pointers,
    #start at the END instead of the front!
    # look for the largest and copy that
    #(working backwards, this way you will never overwrite an element) and
    #time complexity is still O(n) but space is O(1)

        if len(nums1) == 0 and len(nums2) == 0:
            nums1 = []
            return None
        elif len(nums1) == 0:
            for num in nums2:nums1.append(num)
            return None
        elif len(nums2) == 0:return None

        nums1_pointer = m - 1
        nums2_pointer = n - 1
        over_write_pointer = len(nums1) - 1


        while nums1_pointer >= 0 and nums2_pointer >= 0:
            if nums1[nums1_pointer] > nums2[nums2_pointer]:

                nums1[over_write_pointer] = nums1[nums1_pointer]
                over_write_pointer -= 1
                nums1_pointer -= 1

            else:

                nums1[over_write_pointer] = nums2[nums2_pointer]
                over_write_pointer -= 1
                nums2_pointer -= 1

        while nums1_pointer >= 0 :

            nums1[over_write_pointer] = nums1[nums1_pointer]
            nums1_pointer -= 1
            over_write_pointer -= 1

        while nums2_pointer >= 0 :

            nums1[over_write_pointer] = nums2[nums2_pointer]
            nums2_pointer -= 1
            over_write_pointer -= 1



nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

Solution().merge(nums1,m,nums2,n)
print(nums1)
