class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.output = list()
        self.stack = list()

    def preorderTraversal(self, root):

        if root is None: return root

        self.stack.append(root)

        while self.stack:

            cur_root = self.stack.pop()

            if cur_root is None: continue

            self.output.append(cur_root.val)

            self.stack.append(cur_root.right)
            self.stack.append(cur_root.left)


        return self.output

def main():

    root = TreeNode(3)
    root.right = TreeNode(2)
    root.left = TreeNode(1)

    print(Solution().preorderTraversal(root))

if __name__ == "__main__":
    main()
