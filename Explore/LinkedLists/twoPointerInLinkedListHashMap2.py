class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        node_pointers = set()
        node = head

        while node is not None:
            if node in node_pointers: return node
            node_pointers.add(node)
            node = node.next

        return None

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head

    print(Solution().detectCycle(head))

if __name__ == "__main__":
    main()
