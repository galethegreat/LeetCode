class Solution(object):
    def __init__(self):
        self.graph = dict()

    def makeGraph(self, lists):
        for li in lists:
            node = li[0]
            pre_req = li[1:]
            if self.graph.get(node, False):
                for req in pre_req: self.graph[node].append(req)
            else: self.graph[node] = pre_req

    def move_vertex(self, vertex, source_set, destination_set):
        source_set.remove(vertex)
        destination_set.add(vertex)

    def dfs(self, current, white, gray, black):

        self.move_vertex(current, white, gray)

        pre_reqs = self.graph.get(current, [])

        for req in pre_reqs:

            if req in black: continue
            if req in gray: return True
            if self.dfs(req, white, gray, black): return True

        self.move_vertex(current, gray, black)

        return False

    def canFinish(self, numCourses, prerequisites):

        self.makeGraph(prerequisites)

        gray = set()
        black = set()
        white = set()

        for pre_req in prerequisites:
            for req in pre_req: white.add(req)

        while white:
            #gets first node in set, iter wont work cuz set changes size in DFS
            for current_node in white:break

            if self.dfs(current_node, white, gray, black): return False

        return True
