class Solution(object):

    def maxArea(self, height):

        left = 0
        right = len(height) - 1

        water = 0

        left_max = height[left]
        right_max = height[right]

        while left < len(height) and height[left] <= 0:
            left += 1

        while right >= 0 and height[right] <= 0:
            right -= 1

        while left < right:

            if height[left] > left_max:
                left_max = height[left]

            if height[right] > right_max:
                right_max = height[right]

            if left_max <= right_max:
                left += 1
                water += max(0, left_max - height[left])
            else:
                right -= 1
                water += max(0, right_max - height[right])


        return water


def main():

    height = [4,2,0,3,2,5]
    print(Solution().maxArea(height))

if __name__ == "__main__":
    main()
