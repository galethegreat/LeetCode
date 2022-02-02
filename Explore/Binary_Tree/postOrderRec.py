class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.output = list()

    def postorderTraversal(self, root):

        def postOrder(root):

            if root is None: return

            postOrder(root.left)
            postOrder(root.right)
            self.output.append(root.val)

        postOrder(root)

        return self.output

def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(Solution().postorderTraversal(root))

if __name__ == "__main__":
    main()
