class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.sum = None
    def maxPathSum(self, root):
        def path(root):
            if root is None: return 0
            mid = root.val
            left_path = path(root.left)
            right_path = path(root.right)
            optimal_sum =  max(mid, mid+left_path, mid+right_path)
            if self.sum is None or  self.sum < mid + left_path + right_path:
                self.sum = mid + left_path + right_path
            if self.sum is None or self.sum < optimal_sum:
                self.sum = optimal_sum
            return optimal_sum
        path(root)
        return self.sum

def main():

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().maxPathSum(root))

if __name__ == "__main__":
    main()
