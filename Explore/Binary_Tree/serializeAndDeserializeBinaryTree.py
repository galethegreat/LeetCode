class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if root is None: return ""

        serial_output = list()

        que = deque()

        que.append((root))

        while que:
            cur_root = que.popleft()
            if cur_root is None:
                serial_output.append('null')
                continue

            serial_output.append(str(cur_root.val))
            que.append(cur_root.left)
            que.append(cur_root.right)

        return ",".join(serial_output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        vals = data.split(",")
        nodes = iter((None if v == 'null' else TreeNode(int(v))) for v in vals)
        root = next(nodes)
        q = deque([root])

        while q:
            node = q.popleft()

            left = next(nodes)
            if left:
                node.left = left
                q.append(left)

            right = next(nodes)
            if right:
                node.right = right
                q.append(right)

        return root

def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(7)

    ser = Codec().serialize(root)
    print(ser)
    des = Codec().deserialize(ser)
    print(des)
if __name__ == "__main__":
    main()
