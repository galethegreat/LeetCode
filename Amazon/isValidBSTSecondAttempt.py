class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class Solution(object):
    def __init__(self):
        self.isValid = True

    def isValidBST(self, tree):

        def inOrder(root):

            if root is None or self.isValid == False: return None

            left = inOrder(root.left)
            mid = root.val
            right = inOrder(root.right)

            if right is None and left is None: return (mid, mid)

            if left is None and right[0] <= mid: self.isValid = False
            elif right is None and left[1] >= mid: self.isValid = False
            elif (left and right) and (left[1] >= mid or right[0] <= mid): self.isValid = False

            if self.isValid == False: return (mid, mid)
            if left is None: return (min(mid, right[0]) , right[1])
            if right is None: return (left[0], max(mid, left[1]))

            return (left[0], right[1])

        inOrder(tree)

        return self.isValid

tree = Node(3)
tree.left = Node(1)
tree.right = Node(5)
tree.right.left = Node(4)
tree.right.right = Node(6)
tree.left.left = Node(0)
tree.left.right = Node(2)
tree.left.right.right = Node(3)


print(Solution().isValidBST(tree))
