import heapq
import math

class Solution(object):

    def kClosest(self, points, k):
        def distance_from_origin(point):
            x = point[0]
            y = point[1]
            distance = math.sqrt((x-0)**2 + (y-0)**2)
            return distance

        distances = list()
        for point in points:
            heapq.heappush(distances, (distance_from_origin(point), point))

        k_closests_points = list()
        for _ in range(k):
            k_closests_points.append(heapq.heappop(distances)[1])

        return k_closests_points

def main():

    points =  [[3,3],[5,-1],[-2,4]]
    k = 2
    print(Solution().kClosest(points, k))

if __name__ == "__main__":
    main()
