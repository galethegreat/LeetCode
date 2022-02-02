class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.output = list()
        self.stack = list()

    def inorderTraversal(self, root):

        if root is None: return

        while True:

            if root:
                self.stack.append(root)
                root = root.left
            else:
                if len(self.stack) == 0 : return self.output
                root = self.stack.pop()
                self.output.append(root.val)
                root = root.right

def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(Solution().inorderTraversal(root))

if __name__ == "__main__":
    main()
