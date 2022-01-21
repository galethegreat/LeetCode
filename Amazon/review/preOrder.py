# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.stack = list()
    def preorderTraversal(self, root):
        def preOrder(root):
            if root is not None:
                self.stack.append(root.val)
                preOrder(root.left)
                preOrder(root.right)

        preOrder(root)

        return self.stack
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(Solution().preorderTraversal(root))
