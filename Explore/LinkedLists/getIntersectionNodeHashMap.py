class Solution(object):
    def getIntersectionNode(self, head_a, head_b):

        if head_a is None or head_b is None: return None

        visited_nodes = set()

        node = head_a

        while node is not None:
            visited_nodes.add(node)
            node = node.next

        node = head_b

        while node is not None:
            if node in visited_nodes: return node
            node = node.next

        return None
