from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def __init__(self):
        self.que = deque()

    def connect(self, root):
        if root is None: return None

        currrent_level = 0
        self.que.append((root, currrent_level))
        last_node = None

        while self.que:

            currrent_root, new_level = self.que.popleft()

            if currrent_level != new_level:
                last_node = None
                currrent_level = new_level

            if currrent_root is None: continue

            currrent_root.next = last_node
            last_node = currrent_root

            self.que.append((currrent_root.right, currrent_level + 1))
            self.que.append((currrent_root.left, currrent_level + 1 ))

        return root

def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(Solution().connect(root))

if __name__ == "__main__":
    main()
