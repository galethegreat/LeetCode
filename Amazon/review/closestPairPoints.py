import math

def dist(p1, p2):
    p1_x = p1[0]
    p1_y = p1[1]
    p2_x = p2[0]
    p2_y = p2[1]
    return math.sqrt((p2_y - p1_y)**2 + (p2_x - p1_x)**2)

def closest_brute(points):
    min_distance = float('inf')
    p1 = None
    p2 = None
    for point in points:
        for next_point in points:
            if next_point == point:continue
            distance = dist(point, next_point)
            if distance < min_distance:
                min_distance = distance
                p1 = point
                p2 = next_point

    return p1, p2, min_distance

def closestPair(xsorted, ysorted):
    num_of_points= len(xsorted)
    if num_of_points <= 3:
        return closest_brute(xsorted)
    else:
        midpoint_index = num_of_points//2
        midpoint = xsorted[midpoint_index]
        xsorted_left = xsorted[:midpoint_index]
        xsorted_right = xsorted[midpoint_index:]
        ysorted_left = list()
        ysorted_right = list()
        for point in ysorted:
            if point[0] <= midpoint[0]:
                ysorted_left.append(point)
            else:
                ysorted_right.append(point)
        (p1_left, p2_left, delta_left) = closestPair(xsorted_left,ysorted_left)
        (p1_right, p2_right, delta_right) = closestPair(xsorted_right,ysorted_right)
        if delta_left < delta_right:
            p1 = p1_left
            p2 = p1_left
            delta = delta_left
        else:
            p1 = p1_right
            p2 = p1_right
            delta = delta_right
        in_band = [point for point in ysorted if midpoint[0]-delta < point[0] < midpoint[0]+delta]
        for i in range(len(in_band)):
            for j in range(i+1, min(i+7, len(in_band))):
                d = dist(in_band[i], in_band[j])
                if d < delta:
                    (p1, p2, delta) = (in_band[i], in_band[j], d)
        return p1, p2, delta
def main():
    points = [[4,4],[-2,-2],[-3,-4],[-1,3],[2,3],[-4,0],[1,1],[-1,-1],[3, -1], [-4,2], [-2,4]]
    xsorted = sorted(points, key = lambda point: point[0])
    ysorted = sorted(points, key = lambda point: point[1])
    print(closestPair(xsorted, ysorted))
if __name__ == "__main__":
    main()
