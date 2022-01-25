class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        node_pointers = set()
        if head is None: return False
        current_node = head
        node_pointers.add(current_node)
        next_node = head.next

        while next_node is not None:
            if next_node in node_pointers: return True
            node_pointers.add(next_node)
            next_node = next_node.next

        return False

def main():
    head = ListNode(0)
    print(Solution().hasCycle(head))

if __name__ == "__main__":
    main()
