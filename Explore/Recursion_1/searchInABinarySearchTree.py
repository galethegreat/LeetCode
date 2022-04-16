class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        if root is None: return None

        if val == root.val: return root

        root = root.left if val < root.val else root.right

        return searchBST(root)




def main():

if __name__ == '__main__':
    main()
