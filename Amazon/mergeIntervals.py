class Solution(object):

    def merge(self, intervals):
        if len(intervals) <= 1: return intervals

        intervals_toupled = list()
        for index, interval in enumerate(intervals):
            intervals_toupled.append((interval[0], interval[1]))
            intervals_toupled.append(((interval[1]), interval[1]))

        intervals_toupled.sort()
        answer = list()
        isSet = False
        for point in intervals_toupled:

            if isSet:
                if point[0] > end:
                    answer.append([start, end])
                    start, end = point[0], point[1]
                elif point[1] > end:
                    end = point[1]
            else:
                isSet = True
                start, end = point[0], point[1]
        answer.append([start,end])
        return answer

def main():

    intervals =  [[0,4],[1,4]]

    print(Solution().merge(intervals))

if __name__ == "__main__":
    main()
