import heapq
class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.heapK = [num for num in nums]
        heapq.heapify(self.heapK)
        while len(self.heapK) > k:
            heapq.heappop(self.heapK)

    def add(self, val):
        if len(self.heapK) < self.k:
            heapq.heappush(self.heapK,val)

        elif val >= self.heapK[0]:
            heapq.heapreplace(self.heapK,val)

        return self.heapK[0]


K = KthLargest(3, [4, 5, 8, 2])
print(K.add(3))
print(K.add(5))
print(K.add(10))
print(K.add(9))
print(K.add(4))
