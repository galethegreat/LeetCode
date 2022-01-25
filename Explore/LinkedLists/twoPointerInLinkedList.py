class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None: return False
        slow_pointer = head
        fast_pointer = head.next

        while slow_pointer != fast_pointer:
            if fast_pointer is None or fast_pointer.next is None: return False

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next


        return True

def main():
    head = ListNode(0)
    print(Solution().hasCycle(head))

if __name__ == "__main__":
    main()
