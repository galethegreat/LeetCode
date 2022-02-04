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

    root = TreeNode(3)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.left.left = TreeNode(13)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(30)
    root.right.right.left.left = TreeNode(36)
    root.right.right.left.right = TreeNode(37)
    root.left = TreeNode(9)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(11)
    root.left.right.right = TreeNode(12)

    print(Solution().inorderTraversal(root))

if __name__ == "__main__":
    main()
