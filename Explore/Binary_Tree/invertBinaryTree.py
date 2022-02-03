class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def invertTree(self, root):
        if root is None: return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    print(Solution().invertTree(root))

if __name__ == "__main__":
    main()
