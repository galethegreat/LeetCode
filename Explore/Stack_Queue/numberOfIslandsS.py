from collections import deque

class Solution(object):
    def checkChildren(self, grid, t, visited, q):
        r,c = t[0], t[1]
        if c - 1 >= 0 and grid[r][c - 1] not in visited and grid[r][c - 1] == '1':
            q.append((r, c - 1))

        if c + 1 < len(grid[0]) and grid[r][c + 1] not in visited and grid[r][c + 1] == '1':
            q.append((r, c + 1))

        if r - 1 >= 0 and grid[r - 1][c] not in visited and grid[r - 1][c] == '1':
            q.append((r - 1, c))

        if r + 1 < len(grid) and grid[r + 1][c] not in visited and grid[r + 1][c] == '1':
            q.append((r + 1, c))

    def numIslands(self, grid):

        rows = len(grid)
        columns = len(grid[0])

        if columns < 1: #if column is empty, cant have islands
            return 0

        isThereOne = False

        for row in range(rows):#check if there is one '1' grid, if 0 '1', no island
            for column in range(columns):

                if grid[row][column] == '1':
                    isThereOne = True
                    break

            if isThereOne:
                break

        if not isThereOne: return 0

        q = deque()
        vistited = set()
        islands = list()

        for row in range(rows):
            for column in range(columns):
                if (row, column) in vistited: continue

                if grid[row][column] == '0': continue

                else:

                    island = []
                    q.append((row, column))

                    while len(q) > 0:

                        coordinate = q.popleft()
                        if coordinate in vistited : continue

                        r, c = coordinate[0], coordinate[1]
                        t = (r,c)

                        self.checkChildren(grid, t, vistited, q)
                        island.append(coordinate)
                        vistited.add(coordinate)

                    if len(island) > 0: islands.append(island)


        return len(islands)

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

print(Solution().numIslands(grid))
