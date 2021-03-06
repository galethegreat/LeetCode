class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.depth = 0

    def maxDepth(self, root):
        def dfs(root, level):

            if root is None:return

            self.depth = max(self.depth, level)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        if root is None: return self.depth
        dfs(root, 1)


        return self.depth

def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    print(Solution().maxDepth(root))

if __name__ == "__main__":
    main()
