class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():

    def isValidBST(self, root):

        def helper(root, low_bound, max_bound):

            if root is None: return True

            if root.val > low_bound and root.val < max_bound:

                left = helper(root.left, low_bound, root.val )
                right = helper(root.right, root.val, max_bound)

                return left and right

            return False

        return helper(root, float('-inf'), float('inf'))

def main():

    l2 = [7,2,3,8]
    print(Solution().sortArray(l2))

if __name__ == "__main__":
    main()
