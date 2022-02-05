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
        self.flip = False

    def zigzagLevelOrder(self, root):

        if root is None: return

        prev_level = 0
        cur_levl = prev_level + 1
        #temp_ans = list()
        temp_ans = deque()
        self.output.append([root.val])
        self.que.append((root.left, cur_levl))
        self.que.append((root.right, cur_levl))
        self.flip = True
        while self.que:

            if len(self.que) == 0: return self.output

            node_level = self.que.popleft()

            current = node_level[0]
            new_levl = node_level[1]

            if new_levl != cur_levl:
               # if self.flip: temp_ans.reverse()
                self.flip = not(self.flip)
                self.output.append(temp_ans)
                temp_ans = deque()
                #temp_ans = list()
                cur_levl = new_levl

            if current is None: continue

            if self.flip: temp_ans.appendleft(current.val)
            else: temp_ans.append(current.val)

            self.que.append((current.left, cur_levl +1))
            self.que.append((current.right, cur_levl +1))

        return self.output

def main():

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().zigzagLevelOrder(root))

if __name__ == "__main__":
    main()
