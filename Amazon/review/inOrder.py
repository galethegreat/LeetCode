# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.stack = list()
    def inorderTraversal(self, root):
        def inOrder(root):
            if root is not None:

                inOrder(root.left)
                self.stack.append(root.val)
                inOrder(root.right)

        inOrder(root)
        return self.stack

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(Solution().inorderTraversal(root))
