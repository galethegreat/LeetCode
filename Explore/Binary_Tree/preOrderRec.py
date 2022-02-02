class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.output = list()

    def preorderTraversal(self, root):
        def preOrder(root):
            if root is None: return

            self.output.append(root.val)
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)

        return self.output

def main():

    #root = TreeNode(1)
    #root.right = TreeNode(2)
    #root.right.left = TreeNode(3)

    print(Solution().preorderTraversal(root))

if __name__ == "__main__":
    main()
