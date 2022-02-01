class Solution(object):
    # total_size = 12, half = 6 (even)
    #1,2,3,4,5,6,7,8
    #1,2,3,4
    #           left_partition  right_partition
    #combined: [1,1,2,2,3,(3],[4),4,5,6,7,8]  median: 3+4 / 2
    #intial partion is [1,2] from smaller (midpoint) and [1,2,3,4] from larger
    #compare if right index is > smaller if not expand or decrease
    #final partion_from_smaller = [1,2,3] partion_from_larger = [1,2,3]

    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) == 0 and len(nums2) == 0: return 0

        total_size = len(nums1) + len(nums2)
        elements_in_left_partition = total_size // 2

        smaller_array, larger_array = nums1, nums2

        if len(smaller_array) > len(larger_array):
            smaller_array, larger_array = larger_array, smaller_array

        left_pointer, right_pointer = 0, len(smaller_array) - 1

        while True:

            index_of_midpoint_of_smaller_array = (left_pointer + right_pointer) // 2
            index_of_midpoint_of_larger_array = elements_in_left_partition - index_of_midpoint_of_smaller_array - 2

            left_partion_of_smaller_array = smaller_array[index_of_midpoint_of_smaller_array] if index_of_midpoint_of_smaller_array >= 0 else float("-inf")
            right_partion_of_smaller_array = smaller_array[index_of_midpoint_of_smaller_array + 1] if (index_of_midpoint_of_smaller_array + 1) < len(smaller_array) else float("inf")

            left_partion_of_larger_array = larger_array[index_of_midpoint_of_larger_array] if index_of_midpoint_of_larger_array >= 0 else float("-inf")
            right_partion_of_larger_array = larger_array[index_of_midpoint_of_larger_array + 1] if (index_of_midpoint_of_larger_array + 1) < len(larger_array) else float("inf")

            #partion is good
            if left_partion_of_smaller_array <= right_partion_of_larger_array and left_partion_of_larger_array <= right_partion_of_smaller_array:
                #even
                if total_size % 2:
                    return min(right_partion_of_smaller_array, right_partion_of_larger_array)
                #odd
                return (max(left_partion_of_smaller_array, left_partion_of_larger_array) + min(right_partion_of_smaller_array, right_partion_of_larger_array)) / 2

            #partion is bad left partion of smaller is greater than right partion
            elif  left_partion_of_smaller_array > right_partion_of_larger_array:

                right_pointer = index_of_midpoint_of_smaller_array - 1

            else:
                left_pointer = index_of_midpoint_of_smaller_array + 1

    def youtube(self, nums1, nums2):
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

def main():

    nums1 = [1,2]
    nums2 = [3,4]

    print(Solution().findMedianSortedArrays(nums1,nums2))

if __name__ == "__main__":
    main()
