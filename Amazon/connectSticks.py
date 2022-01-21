import heapq
class MedianFinder(object):
    def __init__(self):
        self.heapMin = list()
        self.heapMax = list()

    def addNum(self, num):
        if len(self.heapMax) == 0:
            heapq.heappush(self.heapMax, -num)
        elif len(self.heapMin) == 0:
            if num > - self.heapMax[0]:
                heapq.heappush(self.heapMin, num)
            else:
                heapq.heappush(self.heapMin, - heapq.heappop(self.heapMax))
                heapq.heappush(self.heapMax, -num)
        else:
            if len(self.heapMin) == len(self.heapMax):
                if num >= - self.heapMax[0]:
                    heapq.heappush(self.heapMin, num)
                else:
                    heapq.heappush(self.heapMax, -num)

            elif len(self.heapMax) > len(self.heapMin):
                if num >= - self.heapMax[0]:
                    heapq.heappush(self.heapMin, num)
                else:
                    temp = heapq.heappop(self.heapMax)
                    heapq.heappush(self.heapMax, -num)
                    heapq.heappush(self.heapMin, -temp)
            else:
                if num <= self.heapMin[0]:
                    heapq.heappush(self.heapMax, -num)
                else:
                    temp = heapq.heappop(self.heapMin)
                    heapq.heappush(self.heapMin, num)
                    heapq.heappush(self.heapMax, -temp)

    def findMedian(self):
        if len(self.heapMin) == 0: return -self.heapMax[0]

        if len(self.heapMin) > len(self.heapMax): return self.heapMin[0]

        if len(self.heapMax) > len(self.heapMin): return -self.heapMax[0]

        return (-self.heapMax[0] + self.heapMin[0])/2


M = MedianFinder()
M.addNum(1)

print(M.findMedian())
M.addNum(3)
print(M.findMedian())
