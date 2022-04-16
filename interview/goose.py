class Solution(object):
    def __init__(self):
        self.order_of_dependencies = list()
        self.visited = set()
        self.error = False
    def findOrderOfDependencies(self, pkg_graph, pkg):

        def dfs(graph, pkg):
            self.visited.add(pkg)
            dependencies = graph[pkg]
            if len(dependencies) == 0 :
                self.order_of_dependencies.append(pkg)
                return None

            for dependency in dependencies:
                if pkg in graph[dependency]: self.error = True #learn to throw exception
                if dependency in visited: continue

                dfs(graph, dependency)

            self.order_of_dependencies.append(pkg)


        if pkg not in pkg_graph: return self.order_of_dependencies


        dfs(pkg_graph, pkg)

        return self.order_of_dependencies
