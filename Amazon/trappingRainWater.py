class Solution:
    def trap(self, height):
        if len(height) < 3: return 0
        p1 = 0
        p2 = len(height) - 1
        current_wall_height = 0

        while p1 <= p2:
            if height[p1] <= current_wall_height:
                if p1 + 1 <= p2 and height[p1+1] < current_wall_height:break
                p1 += 1
            else:
                current_wall_height = height[p1]
                if p1 + 1 <= p2 and height[p1+1] < current_wall_height:break
                else: p1 += 1
        if p1 > p2: return 0
        current_wall_height = 0
        while p2 >= p1:
            if height[p2] <= current_wall_height:
                if p2 - 1 >= p1 and height[p2-1] < current_wall_height:break
                p2 -= 1
            else:
                current_wall_height = height[p2]
                if p2 - 1 >= p1 and height[p2-1] < current_wall_height: break
                else: p2 -= 1

        if p2 < p1: return 0

        total_water = 0
        sub_total = 0
        sub_water_list = list()
        current_left_wall = height[p1]
        left_smallest_wall = (height[p1],0)
        current_right_wall = (-1,0)
        index = 0
        p3 = p1
        p3 += 1

        while p3 <= p2:
            while current_left_wall > current_right_wall[0]:
                sub_water_list.append(height[p3])
                index += 1
                if height[p3] < left_smallest_wall[0]:
                    left_smallest_wall = (height[p3],index)
                if p3+1 <= p2 and height[p3+1] > left_smallest_wall[0]:
                    if height[p3+1] >= current_right_wall[0]:
                        current_right_wall = (height[p3+1], index+1)

                elif p3 + 1 >= p2:
                    p3 = p1 + current_right_wall[1]
                    sub_water_list = sub_water_list[:current_right_wall[1]]
                    break
                p3 += 1

            for container in sub_water_list:
                if current_right_wall[0] >= current_left_wall:
                    sub_total += current_left_wall - container
                elif current_right_wall[0] - container < 0: continue
                else: sub_total += current_right_wall[0] - container

            total_water += sub_total
            sub_total = 0
            sub_water_list = list()
            p1 = p3
            current_left_wall = height[p1]
            while p1+1 <= p2 and height[p1+1] > current_left_wall:
                p1 += 1
                p3 += 1
                current_left_wall = height[p1]
            left_smallest_wall = (height[p1],0)
            current_right_wall = (-1,0)
            index = 0
            p3 += 1

        return total_water



height = [4,2,0,3,2,5]
x = Solution().trap(height)
print(x)
