import heapq
class Solution(object):
    def findKthLargest(self,nums,k):
        negative_nums = [-num for num in nums]
        heapq.heapify(negative_nums)
        kt = None
        while k > 0:
            k -= 1
            kt = heapq.heappop(negative_nums)
        return -kt

def main():
    nums = [3,2,1,5,6,4]
    k = 2
    print(Solution().findKthLargest(nums,k))
    return True

if __name__ == "__main__":
    main()
