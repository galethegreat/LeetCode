class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class Solution(object):
    def isValidBST(self,tree):

            def inOrder(tree):

                if tree.left is None and tree.right is None:
                    return (tree.val, tree.val)

                elif tree.left is not None and tree.right is not None:
                    left = inOrder(tree.left)
                    right = inOrder(tree.right)

                elif tree.right is None:
                    right = 'Skip'
                    left = inOrder(tree.left)

                elif tree.left is None:
                    left = 'Skip'
                    right = inOrder(tree.right)

                left_val, right_val = None, None

                if left != 'Skip':
                    if left[0] is not None and left[1] is not None and left[1] < tree.val:
                        left_val = left[0]
                else:
                    left_val = tree.val

                if right != 'Skip':
                    if right[0] is not None and right[1] is not None and right[0] > tree.val:
                        right_val = right[1]
                else:
                    right_val = tree.val

                return (left_val, right_val)

            if tree.left is None and tree.right is None: return True #only root

            ans = inOrder(tree)
            if ans[0] is None or ans[1] is None: return False
            return True

tree = Node(3)
tree.left = Node(1)
tree.right = Node(5)
tree.right.left = Node(4)
tree.right.right = Node(6)
tree.left.left = Node(0)
tree.left.right = Node(2)
tree.left.right.right = Node(3)


print(Solution().isValidBST(tree))
