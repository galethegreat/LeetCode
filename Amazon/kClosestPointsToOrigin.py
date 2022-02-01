import heapq
import math

class Solution(object):

    def kClosest(self, point):
        def distance_from_origin(point):
            x = point[0]
            y = point[1]
            distance = math.sqrt((x-0)**2 + (y-0)**2)
            return distance

        return distance_from_origin(point)

def main():

    intervals = [1,3]

    print(Solution().kClosest(intervals))

if __name__ == "__main__":
    main()
