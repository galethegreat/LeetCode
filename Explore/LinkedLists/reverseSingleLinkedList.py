class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None
        node = head
        if node is None or node.next is None: return head

        while node is not None:
            next = node.next
            node.next = prev
            prev = node
            node = next

        node = prev

        return node


obj = ListNode(1)
obj.next = ListNode(2)


print(Solution().reverseList(obj))
