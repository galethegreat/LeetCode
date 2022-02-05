from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root):
        def longestPath(root):
            if root is None: return 0

            left_path = longestPath(root.left)
            right_path = longestPath(root.right)

            self.diameter = max(self.diameter, left_path + right_path)

            return max(left_path, right_path) + 1

        longestPath(root)

        return self.diameter

def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    print(Solution().diameterOfBinaryTree(root))

if __name__ == "__main__":
    main()
