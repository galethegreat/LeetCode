from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.output = list()
        self.que = deque()
    def checkLevel(self, level):
        p1, p2 = 0, len(level) - 1
        while p1 <= p2:

            if level[p1] != level[p2]: return False
            p1 += 1
            p2 -= 1

        return True

    def isSymmetric(self, root):

        if root is None: return

        prev_level = 0
        cur_levl = prev_level + 1
        temp_ans = list()
        self.que.append((root.left, cur_levl))
        self.que.append((root.right, cur_levl))

        while self.que:

            if len(self.que) == 0: return self.output

            node_level = self.que.popleft()

            current = node_level[0]
            new_levl = node_level[1]

            if new_levl != cur_levl:
                if not self.checkLevel(temp_ans): return False
                temp_ans = list()
                cur_levl = new_levl

            if current is None:
                temp_ans.append(None)
            else:
                temp_ans.append(current.val)
                self.que.append((current.left, cur_levl + 1 ))
                self.que.append((current.right, cur_levl +1 ))

        return True
def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    print(Solution().isSymmetric(root))

if __name__ == "__main__":
    main()
