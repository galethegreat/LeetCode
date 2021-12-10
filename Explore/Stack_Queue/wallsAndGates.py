from collections import deque

class Solution(object):

    def changeNeighbours(self,rooms, coordinate, change_to, q):

        if coordinate[1] - 1 >= 0:
            if rooms[coordinate[0]][coordinate[1] - 1] == 2147483647:
                rooms[coordinate[0]][coordinate[1] - 1] = change_to
                q.append((coordinate[0], coordinate[1] - 1))

        if coordinate[0] - 1 >=0:
            if rooms[coordinate[0] - 1][coordinate[1]] == 2147483647:
                rooms[coordinate[0] - 1][coordinate[1]] = change_to
                q.append((coordinate[0] - 1, coordinate[1]))

        if coordinate[0] + 1 < len(rooms):
            if rooms[coordinate[0] + 1][coordinate[1]] == 2147483647:
                rooms[coordinate[0] + 1][coordinate[1]]  = change_to
                q.append((coordinate[0] + 1, coordinate[1]))

        if coordinate[1] + 1 < len(rooms[0]):
            if rooms[coordinate[0]][coordinate[1] + 1] == 2147483647:
                rooms[coordinate[0]][coordinate[1] + 1] = change_to
                q.append((coordinate[0], coordinate[1] + 1))

    def wallsAndGates(self, rooms):

        rows = len(rooms)
        columns = len(rooms[0])
        if columns < 1:
            print(rooms)
            return None

        if rows == 1 and columns == 1:
            print(rooms)
            return None

        searching = 0 #start searching for gate


        q = deque()

        for row in range(rows):
            for column in range(columns):
                if rooms[row][column] == searching:
                    self.changeNeighbours(rooms, (row, column), searching + 1, q)

        while len(q) > 0:
            coordinate = q.popleft()
            row = coordinate[0]
            column = coordinate[1]
            self.changeNeighbours(rooms, (row, column), rooms[row][column] + 1, q)



        print(rooms)
        return None
# #====================================================================================================
#         #I think this is O(n^4) solution LMAO, it works doe
#         searching = -1
#         isChanged = 1
#         while isChanged > 0:
#
#             searching += 1
#             isChanged = 0
#             for row in range(rows):
#
#                 for column in range(columns):
#
#                     if rooms[row][column] == searching:
#                         isChanged += self.changeNeighbours(rooms, (row, column), searching + 1)
#
#         print(rooms)
#         return None

rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Solution().wallsAndGates(rooms)
