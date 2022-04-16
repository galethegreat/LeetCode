class Solution(object):

    def findShortestPath(self, array):
        def updateNextCoord(current_coord, cost_of_coordinate, array):

            current_cost = cost_of_coordinate[current_coord]

            if current_coord[0] + 1 < len(array):
                coord_down = (current_coord[0]-1, current_coord[1])
                down_val = array[coord_down[0]][coord_down[1]]
                down_cost = current_cost + down_val
                cost_of_coordinate[coord_down] = min(down_cost, cost_of_coordinate.get(coord_down, float('inf') ))

            if current_coord[1] + 1 < len(array[0]):
                coord_right = (current_coord[0], current_coord[1] + 1)
                right_val = array[coord_right[0]][coord_right[1]]
                right_cost = current_cost + right_val
                cost_of_coordinate[coord_right] = min(right_cost, cost_of_coordinate.get(right_cost, float('inf') ))


        cost_of_coordinate = dict()

        nums_rows = len(array)
        nums_of_col = len(array[0])

        start_coord = (0, 0)

        end_coord = (nums_rows - 1, nums_of_col - 1)
        cost_of_coordinate[start_coord]

        for row in range(nums_rows):
            for col in range(nums_of_col):
                current_coord = (row, col)
                updateNextCoord(current_coord, cost_of_coordinate, array)

        return cost_of_coordinate[end_coord]
