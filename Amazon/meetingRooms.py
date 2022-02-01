class Solution(object):

    def canAttendMeetings(self, intervals):

        if len(intervals) <= 1: return True

        intervals_toupled = list()

        for interval in intervals:
            intervals_toupled.append((interval[0],interval[1]))
            intervals_toupled.append((interval[1],interval[1]))

        intervals_toupled.sort()
        start, end = None, None

        for point in intervals_toupled:
            if start is None:
                start = point[0]
                end =  point[1]
            else:
                if point[0] >= start and point[0] != point[1]: return False
                else: start = None

        return True

def main():

    intervals = [[0,30],[5,10],[15,20]]

    print(Solution().canAttendMeetings(intervals))

if __name__ == "__main__":
    main()
