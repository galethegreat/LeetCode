from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms):
        keys = set()
        visited = set()

        next_rooms = deque()
        for key in rooms[0]:
            keys.add(key)
            next_rooms.append(key)

        visited.add(0)
        while len(next_rooms) > 0:
            next_room = next_rooms.popleft()
            if next_room not in visited:
                visited.add(next_room)
                for key in rooms[next_room]:
                    keys.add(key)
                    if key not in visited:
                        next_rooms.append(key)
        for room in range(len(rooms)):
            if room in visited:continue
            else: return False
        return True

rooms = [[1,3],[3,0,1],[2],[2]]
print(Solution().canVisitAllRooms(rooms))
