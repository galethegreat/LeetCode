class Solution(object):

    def maxArea(self, height):

        stack = list()
        water = 0

        for index, bar in enumerate(height):

            while stack and bar > height[stack[-1]]:

                top_bar_index = stack.pop()
                top_bar_height = height[top_bar_index]

                if not stack: break

                distance = index - stack[-1] - 1

                water += (min(height[stack[-1]], bar) - top_bar_height ) * distance

            stack.append(index)

        return water


def main():

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().maxArea(height))

if __name__ == "__main__":
    main()
