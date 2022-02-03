from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.que = deque()
        self.levels = list()


    def rightSideView(self, root):
        if root is None: return None

        currrent_level = 0
        self.que.append((root, currrent_level))
        level_output = list()

        while self.que:

            currrent_root_and_level = self.que.popleft()
            currrent_root, new_level = currrent_root_and_level[0], currrent_root_and_level[1]

            if currrent_root is None: continue

            if currrent_level != new_level:
                self.levels.append(level_output[0])
                level_output = []
                currrent_level = new_level

            level_output.append(currrent_root.val)
            self.que.append((currrent_root.right, currrent_level + 1))
            self.que.append((currrent_root.left, currrent_level + 1 ))

        if len(level_output) > 0:    self.levels.append(level_output)

        return self.levels

def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    #root.right.left = TreeNode(4)
    root.right.right = TreeNode(4)
    #root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.left.left = TreeNode(10)

    print(Solution().rightSideView(root))

if __name__ == "__main__":
    main()
