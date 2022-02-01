class Solution(object):

    def search(self, nums, target):

        def binSearchWithOffset(l, r, nums, target, offset):

            while l <= r:

                mid  = l + (r - l) // 2
                if mid > len(nums) -1:
                    if nums[mid-offset] == target: return mid-offset
                    if nums[mid-offset] < target: l = mid + 1
                    if nums[mid-offset] > target: r = mid -1
                else:
                    if nums[mid] == target: return mid
                    if nums[mid] < target: l = mid + 1
                    if nums[mid] > target: r = mid - 1

            return -1

        if len(nums) == 1: return 0 if nums[0] == target else -1

        l, r = 0, len(nums) -1

        if nums[l] <  nums[r]:return binSearchWithOffset(l,r,nums,target,0)

        isCondtion = False # name it better
        while not isCondtion:

            mid  = l + (r - l) // 2
            if nums[mid] == target: return mid

            elif mid + 1 < len(nums):

                if nums[mid] > nums[mid+1]: isCondtion = mid + 1

                elif nums[l] < nums[mid]:
                    l = mid + 1

                else:
                    r = mid - 1

            else: isCondtion = mid

        l = isCondtion
        r = len(nums) - 1  + l
        return binSearchWithOffset(l,r,nums,target,len(nums))

def main():

    nums =  [1,3]
    target = 2

    print(Solution().search(nums,target))

if __name__ == "__main__":
    main()
