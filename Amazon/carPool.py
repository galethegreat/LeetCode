import heapq

class Solution(object):

    def carPooling(self, trips, capacity):
        if len(trips) < 1: return True

        trips.sort(key = lambda x: x[1])
        car = list()

        for trip in trips:

            if len(car) == 0:

                heapq.heappush(car, (trip[2], trip[1], trip[0]))
                capacity -= trip[0]

            elif trip[1] < car[0][0]:

                if trip[2] > car[0][1]:
                    heapq.heappush(car, (trip[2], trip[1], trip[0]))

                capacity -= trip[0]

            elif trip[1] >= car[0][0]:

                while len(car) > 0 and trip[1] >= car[0][0]:
                    capacity += heapq.heappop(car)[2]

                heapq.heappush(car, (trip[2], trip[1], trip[0]))
                capacity -= trip[0]

            if capacity < 0: return False

        return True

def main():

    trips = [[2,1,5],[3,3,7]]
    capacity = 4
    print(Solution().carPooling(trips, capacity))

if __name__ == "__main__":
    main()
