class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    def __init__(self):
        self.root_index = dict()

    def buildTree(self, inorder, preorder):

        def helper(in_left, in_right):

            if  in_left > in_right : return None

            root_value = que.popleft()

            index = self.root_index[root_value]
            print(root_value)
            root = TreeNode(root_value)

            root.left = helper(in_left, index - 1)
            root.right = helper(index +1, in_right )

            return root

        self.root_index = {root:index for index, root in enumerate(inorder)}
        que = deque(preorder)

        return helper(0, len(self.root_index)-1)

def main():

    inorder = [9,3,15,20,7]
    preorder =  [3,9,20,15,7]
    root = (Solution().buildTree(inorder, preorder))
    print(f"Root Val: {root.val} Left: {root.left.val} Right: {root.right.val}")

if __name__ == "__main__":
    main()
