import heapq

class Solution(object):

    def minMeetingRooms(self, intervals):

        if len(intervals) < 1: return 0
        if len(intervals) == 1: return 1

        intervals.sort()
        rooms = [intervals[0][1]]

        for interval in intervals[1:]:

            if interval[0] >= rooms[0]:
                heapq.heappop(rooms)
                heapq.heappush(rooms, interval[1])

            else:
                heapq.heappush(rooms, interval[1])

        return len(rooms)

def main():

    intervals = [[7,10],[2,4]]

    print(Solution().minMeetingRooms(intervals))

if __name__ == "__main__":
    main()
