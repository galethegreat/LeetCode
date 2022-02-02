class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.output = list()

    def inorderTraversal(self, root):
        def inOrder(root):
            if root is None: return

            inOrder(root.left)
            self.output.append(root.val)
            inOrder(root.right)

        inOrder(root)

        return self.output

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
