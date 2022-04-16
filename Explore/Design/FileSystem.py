class Node:

    def __init__(self, name: str, value: int):

        self.name = name
        self.value = value
        self.children = dict()

class FileSystem:
    def __init__(self):

        self.main = Node('', -1)

    def createPath(self, path: str, value: int) -> bool:

        if not path or path[0] != "/":
            return False

        main = self.main
        path_nodes = path[1:].split("/")

        if not path_nodes[-1]: return False

        for node in path_nodes[0:(len(path_nodes)-1)]:
            if not node or node not in main.children: return False
            main = main.children[node]

        if path_nodes[-1] in main.children: return False

        main.children[path_nodes[-1]] = Node(path_nodes[-1], value)

        return True

    def get(self, path: str) -> int:

        if not path or path[0] != "/":
            return -1

        main = self.main
        path_nodes = path[1:].split("/")

        for node in path_nodes[0:(len(path_nodes))]:
            if not node or node not in main.children: return -1
            main = main.children[node]

        return main.value
