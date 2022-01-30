import heapq
class Solution(object):
    def connectSticks(self, sticks):
        if len(sticks) == 1: return 0
        cost = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            stick_1 = heapq.heappop(sticks)
            stick_2 = heapq.heappop(sticks)
            new_stick = stick_1 + stick_2
            cost += new_stick
            heapq.heappush(sticks,new_stick)
        return cost

sticks = [5]
print(Solution().connectSticks(sticks))
