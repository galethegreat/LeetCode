class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.output = list()
        self.stack = list()

    def postorderTraversal(self, root):
        if root is None: return

        current = root

        while current is not None or len(self.stack) > 0:

            if current:
                self.stack.append(current)
                current = current.left

            else:

                temp = self.stack[-1].right
                if temp is None:

                    temp = self.stack.pop()
                    self.output.append(temp.val)

                    while len(self.stack) != 0 and temp == self.stack[-1].right:
                        temp  = self.stack.pop()
                        self.output.append(temp.val)

                else:
                    current = temp

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
