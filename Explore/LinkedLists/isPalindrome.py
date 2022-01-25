class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
     def isPalindrome(self, head):
        if head is None: return True
        if head.next is None: return True
        if head.next.next is None: return head.val == head.next.val
        size = 0
        node = head

        while node is not None:
            node = node.next
            size += 1
        midpoint = size // 2
        index = 1
        node = head
        while index < midpoint:
            node = node.next
            index += 1

        reverse_node_head = node.next
        node.next = None
        prev = None
        while reverse_node_head is not None:
            next_node = reverse_node_head.next
            reverse_node_head.next = prev
            prev = reverse_node_head
            reverse_node_head = next_node
        reverse_node_head = prev

        node_head = head
        node_reverse = reverse_node_head
        while node_head is not None and node_reverse is not None:
            if node_head.val != node_reverse.val: return False
            node_head = node_head.next
            node_reverse = node_reverse.next
        return True

def main():
    head  = ListNode(1)
    head.next = ListNode(1)
    head.next.next  = ListNode(2)
    head.next.next.next   = ListNode(1)
    head.next.next.next.next   = ListNode(1)
    print(Solution().isPalindrome(head))

if __name__ == "__main__":
    main()
