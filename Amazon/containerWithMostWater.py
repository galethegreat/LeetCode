class Solution:
    def maxArea(self, height):

        p1 = 0
        p2 = len(height) - 1
        distance = p2 - p1
        container_wall = min(height[p1], height[p2])
        max_area = distance * container_wall

        while p1 != p2:

            distance = p2 - p1
            container_wall = min(height[p1], height[p2])
            current_area = distance * container_wall
            if current_area > max_area: max_area = current_area

            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return max_area

def main():
    height =  [1,8,6,2,5,4,8,3,7]

    print((Solution().maxArea(height)))

if __name__ == "__main__":
    main()
