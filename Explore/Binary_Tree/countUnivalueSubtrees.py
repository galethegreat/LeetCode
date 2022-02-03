class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):

        self.count = 0

    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def dfs(root):

            if root is None: return None

            if root.left is None and root.right is None:
                self.count += 1
                return root.val

            left = dfs(root.left)
            right = dfs(root.right)

            if left is None: left = right
            elif right is None: right = left

            if left == right and left == root.val:
                 self.count += 1
                 return root.val
            else:
                 return float("-inf")

        if root is None: return 0

        dfs(root)

        return self.count
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
