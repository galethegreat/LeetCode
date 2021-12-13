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
        def DFS(row,column,visited,grid,next,part_of_island):

            if len(next) > 0:
                coordinate = next.pop()
                if grid[coordinate[0]][coordinate[1]] == '1' and (coordinate[0],coordinate[1]) not in visited:

                    visited.add(coordinate)
                    children = findChildren(coordinate[0],coordinate[1],grid,visited)
                    for child in children:
                        next.append(child)
                        DFS(child[0],child[1],visited,grid,next,part_of_island)
                    part_of_island.append((row,column))
            else:
                return None



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
        next_coordinate = list()

        for row in range(rows):

            for column in range(columns):

                if (row,column) in visited:continue
                elif grid[row][column] == "0":continue
                else:
                    island = []
                    next_coordinate.append((row,column))
                    DFS(row,column,visited,grid,next_coordinate,island)
                    if len(island) > 0: islands.append(island)
        print(islands)
        return len(islands)


grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(Solution().numIslands(grid))
