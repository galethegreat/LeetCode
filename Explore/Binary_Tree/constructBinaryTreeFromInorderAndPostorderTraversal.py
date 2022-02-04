class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.root_index = dict()

    def buildTree(self, inorder, preorder):

        def helper(in_left, in_right):

            if in_left > in_right: return None

            root_value = preorder.pop()

            index = self.root_index[root_value]
            root = TreeNode(root_value)
            root.right = helper(index +1, in_right )
            root.left = helper(in_left, index - 1)

            return root
           
        self.root_index = {root:index for index, root in enumerate(inorder)}


        return helper(0, len(self.root_index)-1)

def main():

    inorder = [9,3,15,20,7]
    preorder = [9,15,7,20,3]
    print(Solution().buildTree(inorder, preorder))

if __name__ == "__main__":
    main()
