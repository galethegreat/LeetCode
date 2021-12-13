class Solution(object):
    def numIslands(self, grid):

        def findChildren(row,column,grid,visited):
            children = list()
            if row - 1 >= 0 and grid[row-1][column] == '1' and (row-1,column) not in visited:
                children.append((row-1,column))
            if row + 1 < len(grid) and grid[row+1][column] == '1' and (row+1,column) not in visited:
                children.append((row+1,column))
            if column - 1 >= 0 and grid[row][column-1] == '1' and (row,column-1) not in visited:
                children.append((row,column-1))
            if column + 1 < len(grid[0]) and grid[row][column+1] == '1' and (row,column+1) not in visited:
                children.append((row,column+1) )
            return children
        #
        # def DFS(row,column,visited,grid):
        #     if (row,column) in visited:
        #         return []
        #     if grid[row][column] == '1':
        #         part_of_island = []
        #         visited.add((row,column))
        #         children = findChildren(row,column,grid,visited)
        #         for child in children:
        #             island_part = DFS(child[0],child[1],grid,visited)
        #             if len(island_part) > 0 :
        #                 part_of_island.append(island_part)
        #
        #         part_of_island.append((row,column))
        #         return part_of_island
        #
        #     else:
        #         return []

        rows = len(grid)
        columns =  len(grid[0])
        isThereOne = False

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == '1':
                    isThereOne = True
                    break
            if isThereOne:break

        if not isThereOne:return 0

        if columns == 0:return 0

        visited = set()
        islands = list()

        for row in range(rows):

            for column in range(columns):

                if (row,column) in visited:continue
                elif grid[row][column] == "0":continue
                else:
                    island = []
                    next_coordinate = list()
                    next_coordinate.append((row,column))
                    while len(next_coordinate) > 0:
                        coordinate = next_coordinate.pop()
                        island.append(coordinate)
                        visited.add(coordinate)
                        children = findChildren(coordinate[0],coordinate[1],grid,visited)
                        for child in children:
                            next_coordinate.append(child)

                    if len(island) > 0: islands.append(island)
        return len(islands)

        
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(Solution().numIslands(grid))
