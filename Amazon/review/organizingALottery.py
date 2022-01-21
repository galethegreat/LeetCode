# Python3 program to find the number
# of segments covering each point

# Function to print an array
def PrintArray(n, arr):

    for i in range(n):
        print(arr[i], end = " ")

# Function prints number of segments
# covering by each points
def NumberOfSegments(segments, points, s, p):

    pts = []
    seg = []

    # Pushing points and index in
    # vector as a pairs
    for i in range(p):
        pts.append([points[i], i])

    for i in range(s):

        # (l, +1)
        seg.append([segments[i][0], 1])

        # (r+1, -1)
        seg.append([segments[i][1] + 1, -1])

    # Sort the vectors
    #print(seg)
    seg.sort(reverse = True)
    pts.sort(reverse = False)

    count = 0
    ans = [0 for i in range(p)]

    for i in range(p):
        x = pts[i][0]

        while(len(seg) != 0 and seg[len(seg) - 1][0] <= x):

            count += seg[-1][1]
            seg.pop()

        ans[pts[i][1]] = count

    # Print the answer
    PrintArray(p, ans)

# Driver code
if __name__ == '__main__':

    # Initializing vector of pairs
    seg = [[1,3],[2,4],[5,7]]

    point = [ 0, 2, 5 ]

    s = len(seg)
    p = len(point)

    NumberOfSegments(seg, point, s, p)
