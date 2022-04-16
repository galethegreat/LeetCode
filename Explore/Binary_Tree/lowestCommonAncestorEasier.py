class Solution:

    def __init__(self):

        self.ancestor = None

    def lowestCommonAncestor(self, root, p, q):
        def dfs(root, p, q):
            if root is None: return False

            mid_node = root in [p, q]
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            if left + right + mid_node >=2: self.ancestor = root

            return mid_node | left | right


        if root in (p or q): return root
        dfs(root, p, q)
        return self.ancestor
