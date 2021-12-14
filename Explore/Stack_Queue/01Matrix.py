from collections import deque
class Solution:
    def updateMatrix(self, mat):
        def updateNeighbours(mat,coordinate,q,visited):
            r, c = coordinate[0], coordinate[1]
            if r - 1 >= 0 and (r-1, c) not in visited and mat[r-1][c] == float('inf'):
                mat[r-1][c] = mat[r][c] + 1
                q.append((r-1, c))
            if c - 1 >= 0 and (r,c-1) not in visited and mat[r][c-1] == float('inf'):
                mat[r][c-1] = mat[r][c] + 1
                q.append((r, c-1))
            if r + 1 < len(mat) and (r+1,c) not in visited and mat[r+1][c] == float('inf'):
                mat[r+1][c] = mat[r][c] + 1
                q.append((r+1, c))
            if c + 1 < len(mat[0]) and (r,c+1) not in visited and mat[r][c+1] == float('inf'):
                mat[r][c+1] = mat[r][c] + 1
                q.append((r, c+1))

        rows = len(mat)
        columns = len(mat[0])
        isThereOne = False

        for row in range(rows):
            for column in range(columns):
                if mat[row][column] == 1:
                    isThereOne = True
                    break
            if isThereOne:break
        if not isThereOne:return mat

        distance_matrix = [[float('inf') for i in range(columns)] for j in range(rows)]
        q = deque()
        visited = set()
        for row in range(rows):
            for column in range(columns):
                if mat[row][column] == 1:
                    mat[row][column] = float('inf')

        for row in range(rows):
            for column in range(columns):
                if mat[row][column] == 0:
                    q.append((row,column))

        while len(q) > 0:
            coordinate = q.popleft()
            visited.add(coordinate)
            updateNeighbours(mat,coordinate,q,visited)

        return mat


matrix = [[1,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,0,0,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,0,1,0,1,1,1,1]]

print(Solution().updateMatrix(matrix))
