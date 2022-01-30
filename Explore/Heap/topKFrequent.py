import heapq
class Solution(object):
    def topKFrequent(self,nums,k):
        num_and_freq = dict()

        for num in nums:
            num_and_freq[num] = num_and_freq.get(num, 0) + 1

        freq_and_num = sorted([(freq,num) for num,freq in num_and_freq.items()], reverse=True)
        ans = list()
        for i in range(k):
            ans.append(freq_and_num[i][1])

        return ans


def main():
    nums =  [1,1,1,2,2,3]
    k = 2
    print(Solution().topKFrequent(nums,k))
    return True

if __name__ == "__main__":
    main()
