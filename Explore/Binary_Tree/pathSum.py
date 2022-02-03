class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(root, targetSum, currentSum):

            if root is None: return False

            currentSum += root.val

            if currentSum == targetSum and (root.left is None and root.right is None): return True

            return dfs(root.left, targetSum, currentSum) or dfs(root.right, targetSum, currentSum)


        if root is None: return False

        return dfs(root, targetSum, 0)

def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    targetSum = 22
    print(Solution().hasPathSum(root, targetSum))

if __name__ == "__main__":
    main()
