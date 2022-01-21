from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self,nums,k):
        nums_and_freq = dict()
        for num in nums:
            nums_and_freq[num] = nums_and_freq.get(num, 0) + 1

        freq_and_nums = [(-freq, num) for num, freq in nums_and_freq.items()]
        heapq.heapify(freq_and_nums)
        top_k_freq_and_nums = list()

        while k > 0:
            k -= 1
            top_k_freq_and_nums.append(heapq.heappop(freq_and_nums))
        answer = [freq_num[1] for freq_num in top_k_freq_and_nums]

        return answer

        #the chad solution:
        # if k == len(nums):  return nums
        # count = Counter(nums)
        # return heapq.nlargest(k, count.keys(), key=count.get)


def main():
    nums =  [1,1,1,2,2,3]
    k = 2
    print(Solution().topKFrequent(nums,k))
    return True

if __name__ == "__main__":
    main()
