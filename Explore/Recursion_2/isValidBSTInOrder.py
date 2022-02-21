class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def __init__(self):

        self.prev = None

    def isValidBST(self, root):

        if root is None: return True

        if not self.isValidBST(root.left): return False

        if self.prev is not None and self.prev >= root.val: return False

        self.prev = root.val

        return self.isValidBST(root.right)


def main():

    l2 = [7, 2, 3, 8]
    print(Solution().sortArray(l2))

if __name__ == "__main__":
    main()
