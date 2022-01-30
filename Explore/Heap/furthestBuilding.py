import heapq

class Solution(object):
    def furthestBuilding(self, buildings, bricks, ladders):
        height_differences = list()

        if len(buildings) == 1: return 0

        for index, building in enumerate(buildings):
            cur = building
            if index+1 < len(buildings): next = buildings[index+1]
            else:  break
            if next-cur > 0:
                if len(height_differences) < ladders:
                    heapq.heappush(height_differences, ((next-cur), index))
                else:
                    distance = next-cur
                    use_brick = heapq.heappushpop(height_differences, (distance, index))
                    bricks -= use_brick[0]
                    if bricks < 0: return index

        return index


def main():
    buildings = [4,12,2,7,3,18,20,3,19]
    bricks = 10
    ladders = 2
    print(Solution().furthestBuilding(buildings,bricks, ladders))

if __name__ == "__main__":
    main()
