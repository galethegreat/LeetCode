from collections import deque

class MovingAverage:
    def __init__(self,max):
        self.values = deque([],max)
        self.sum = 0
        self.max = max
    def next(self,value):

        if len(self.values) == self.max:
            self.sum -= self.values.popleft()

        self.values.append(value)
        self.sum += value


        return self.sum/len(self.values)

move = MovingAverage(3)
print(move.next(1))
print(move.next(10))
print(move.next(3))
print(move.next(5))
