import heapq
class Solution:
    def lastStoneWeight(self, stones):
        if len(stones) <= 1: return stones[0]
        elif len(stones) == 2:
            if stones[0] == stones[1]:
                return 0
            else:
                return max(stones[1],stones[0]) - min(stones[1],stones[0])
        stones_neg = [-stone for stone in stones]

        heapq.heapify(stones_neg)

        while len(stones_neg) > 1:
            large_stone = -(heapq.heappop(stones_neg))
            small_stone = -(heapq.heappop(stones_neg))
            if large_stone == small_stone: continue
            else:
                large_stone -= small_stone
                heapq.heappush(stones_neg, -large_stone)
        if len(stones_neg) > 0:
            return -stones_neg[0]
        else:
            return 0

stones =  [3,7,2]
print(Solution().lastStoneWeight(stones))
